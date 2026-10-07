"""Validate all notebooks against the graphics backend of the current branch.

python -X utf8 tools/verify_notebooks.py [--execute] [--weeks 5 6 7]
Use the Python environment installed from this branch's requirements.txt.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
import tempfile

import nbformat

BASE = Path(__file__).resolve().parents[1]
VARIANT = json.loads((BASE / 'NOTEBOOK_VARIANT.json').read_text(encoding='utf-8'))
BACKEND = VARIANT['backend']
AUTHOR = 'ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET'


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def code_tree(source):
    return ast.parse('\n'.join(line for line in source.splitlines()
                               if not line.lstrip().startswith(('%', '!'))))


def check_graphics_source(source, context):
    tree = code_tree(source)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split('.')[0] for alias in node.names)
            if BACKEND == 'plotnine':
                require(not any(alias.name.startswith('pandas.plotting') for alias in node.names),
                        f'{context}: pandas.plotting import')
        elif isinstance(node, ast.ImportFrom):
            imports.add((node.module or '').split('.')[0])
            if BACKEND == 'plotnine':
                require(not (node.module or '').startswith('pandas.plotting'), f'{context}: pandas.plotting import')
        if BACKEND == 'plotnine' and isinstance(node, ast.Attribute):
            require(node.attr not in {'plot', 'plotting', 'hist', 'boxplot'},
                    f'{context}: implicit non-Plotnine plotting')
    forbidden = {'matplotlib', 'plotly', 'seaborn', 'altair', 'bokeh'} if BACKEND == 'plotnine' else {'plotnine', 'seaborn', 'altair', 'bokeh'}
    require(not imports.intersection(forbidden), f'{context}: graphics imports from another backend')
    if BACKEND == 'plotnine':
        require(not re.search(r'\b(?:plt|pio|go|px)\.', source), f'{context}: other graphics backend call')
    return imports


def check_markdown_preservation(left, right, filename, approvals):
    # These cells were reviewed for backend wording/snippets. Their exact final
    # text is frozen so a later prose-only answer change also fails validation.
    original = left.source.replace(r' <\hat y>', '')
    current = right.source.replace(r' <\hat y>', '')
    if original == current:
        return
    approval = approvals.get(filename, {}).get(right.id)
    require(approval is not None, f'{filename}: unapproved theory/exercise edit at {right.id}')
    digest = lambda text: hashlib.sha256(text.encode('utf-8')).hexdigest()
    require(approval['original_sha256'] == digest(original) and approval['current_sha256'] == digest(current),
            f'{filename}: reviewed Markdown changed at {right.id}')


def math_expressions(source):
    # Remove the stray marker found in the original W4 SSE formula. Both
    # branches use the standard squared-residual expression after correction.
    source = source.replace(r' <\hat y>', '')
    return re.findall(r'\$\$.*?\$\$|\$(?!\$)[^$]+?\$', source, flags=re.S)


def source_metadata(cell):
    return {key: value for key, value in cell.metadata.items() if key != 'execution'}


def baseline_notebook(name):
    commit = VARIANT['original_content_commit']
    result = subprocess.run(['git', 'show', f'{commit}:{name}'], cwd=BASE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return nbformat.reads(result.stdout.decode('utf-8'), as_version=4) if result.returncode == 0 else None


def validate(path):
    from nbconvert.filters import markdown2html
    n = nbformat.read(path, as_version=4)
    nbformat.validate(n)
    ids = [cell.id for cell in n.cells]
    require(len(ids) == len(set(ids)), f'{path.name}: duplicate cell IDs')
    markdown = '\n'.join(c.source for c in n.cells if c.cell_type == 'markdown')
    require(AUTHOR in markdown, f'{path.name}: missing author')
    require(not any(char in markdown for char in ('\x00', '\x08', '\x0b', '\x0c')),
            f'{path.name}: invalid control characters in Markdown')
    require(r'<\hat y>' not in markdown, f'{path.name}: stray marker in SSE formula')
    code_cells = [c for c in n.cells if c.cell_type == 'code' and c.source.strip()]
    imports = set()
    for c in code_cells:
        imports.update(check_graphics_source(c.source, f'{path.name}: code {c.id}'))
        require(c.execution_count is not None, f'{path.name}: unexecuted cell {c.id}')
        for output in c.outputs:
            require(output.output_type != 'error', f'{path.name}: execution error at {c.id}')
            if output.output_type == 'stream' and output.name == 'stderr':
                require(not output.text.strip(), f'{path.name}: stderr at {c.id}: {output.text}')
    if BACKEND == 'plotnine':
        require('plotnine' in imports, f'{path.name}: missing Plotnine import')
        require(not imports.intersection({'matplotlib', 'plotly', 'seaborn', 'altair', 'bokeh'}),
                f'{path.name}: imports from another plotting backend: {imports}')
        require(not re.search(r'\b(?:plt|pio|go|px)\.', markdown),
                f'{path.name}: old plotting code in Markdown')
    else:
        require('matplotlib' in imports or 'plotly' in imports, f'{path.name}: missing expected graphics backend')
        require(not imports.intersection({'plotnine', 'seaborn', 'altair', 'bokeh'}),
                f'{path.name}: graphics imports outside Matplotlib/Plotly')
    images = 0
    details = 0
    for c in n.cells:
        if c.cell_type != 'markdown':
            continue
        # Remove Markdown blockquote prefixes before checking Python snippets.
        unquoted = re.sub(r'^\s*>\s?', '', c.source, flags=re.M)
        for snippet in re.findall(r'```(?:python|py)\s*\n(.*?)```', unquoted, flags=re.S):
            check_graphics_source(snippet, f'{path.name}: Markdown {c.id}')
        if '<details' in c.source:
            blocks = re.findall(r'<details[^>]*>(.*?)</details>', markdown2html(c.source), flags=re.S)
            require(len(blocks) == c.source.count('<details'), f'{path.name}: lost answer block {c.id}')
            for block in blocks:
                answer = re.sub(r'<summary[^>]*>.*?</summary>', '', block, flags=re.S)
                require(bool(re.sub(r'<[^>]*>', '', answer).strip()), f'{path.name}: empty answer block {c.id}')
            details += len(blocks)
        targets = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', c.source)
        targets += re.findall(r'<img[^>]+src=[\"\x27]([^\"\x27]+)', c.source)
        for target in targets:
            if target.startswith('attachment:'):
                require(target[11:] in c.get('attachments', {}), f'{path.name}: missing attachment {target}')
            elif not target.startswith(('http://', 'https://', 'data:')):
                require((BASE / target).is_file(), f'{path.name}: missing image {target}')
            images += 1
    week = int(re.match(r'W(\d+)_', path.name).group(1))
    page_count = {5: 93, 6: 80, 7: 94}.get(week)
    if page_count:
        pages = {p for c in n.cells for p in c.metadata.get('source_pages', [])}
        require(pages == set(range(1, page_count + 1)), f'{path.name}: slide coverage changed')
    outputs = [o for c in code_cells for o in c.outputs]
    pngs = sum('image/png' in o.get('data', {}) for o in outputs)
    plotly = sum('application/vnd.plotly.v1+json' in o.get('data', {}) for o in outputs)
    require(pngs + plotly > 0, f'{path.name}: no saved plot outputs')
    require(BACKEND != 'plotnine' or (pngs > 0 and plotly == 0), f'{path.name}: wrong saved plot backend')
    baseline = baseline_notebook(path.name)
    changed_markdown = []
    changed_code = []
    if baseline:
        approvals = json.loads((BASE / 'qa/GRAPHICS_MARKDOWN_CHANGES.json').read_text(encoding='utf-8'))
        require([c.id for c in baseline.cells] == ids, f'{path.name}: source cell IDs/order changed')
        for left, right in zip(baseline.cells, n.cells):
            require(left.cell_type == right.cell_type, f'{path.name}: cell type changed at {right.id}')
            require(source_metadata(left) == source_metadata(right), f'{path.name}: source metadata changed at {right.id}')
            require(left.get('attachments', {}) == right.get('attachments', {}),
                    f'{path.name}: illustration attachments changed at {right.id}')
            if left.source != right.source:
                (changed_markdown if right.cell_type == 'markdown' else changed_code).append(right.id)
            if right.cell_type == 'markdown':
                check_markdown_preservation(left, right, path.name, approvals)
                require(math_expressions(left.source) == math_expressions(right.source),
                        f'{path.name}: mathematical expression changed at {right.id}')
        original_ids = sorted(re.findall(r'W\d{2}-[A-Z]+\d+', '\n'.join(c.source for c in baseline.cells if c.cell_type == 'markdown')))
        require(original_ids == sorted(re.findall(r'W\d{2}-[A-Z]+\d+', markdown)),
                f'{path.name}: exercise IDs changed')
    return {'file': path.name, 'week': week, 'backend': BACKEND, 'cells': len(n.cells),
            'code_cells': len(code_cells), 'png_outputs': pngs, 'plotly_outputs': plotly,
            'source_illustrations': images, 'answer_blocks': details, 'slide_pages': page_count,
            'execution_outputs_valid': True, 'baseline_available': baseline is not None,
            'mathematical_expressions_preserved': True if baseline else None,
            'source_ids_metadata_attachments_preserved': True if baseline else None,
            'changed_markdown_ids': changed_markdown, 'changed_code_ids': changed_code}


def execute(path):
    from nbclient import NotebookClient
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpecManager
    n = nbformat.read(path, as_version=4)
    with tempfile.TemporaryDirectory(prefix='xstk-kernel-') as directory:
        spec = Path(directory) / 'xstk-active'
        spec.mkdir()
        (spec / 'kernel.json').write_text(json.dumps({
            'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
            'display_name': 'XSTK active Python', 'language': 'python'}), encoding='utf-8')
        km = KernelManager(kernel_name='xstk-active', kernel_spec_manager=KernelSpecManager(kernel_dirs=[directory]))
        try:
            NotebookClient(n, km=km, timeout=360, resources={'metadata': {'path': str(BASE)}}).execute()
        finally:
            if km.has_kernel:
                km.shutdown_kernel(now=True)
    nbformat.write(n, path)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='Run from a fresh kernel and save outputs')
    parser.add_argument('--weeks', nargs='+', type=int)
    args = parser.parse_args(argv)
    results = []
    for path in sorted(BASE.glob('*.ipynb')):
        week = int(re.match(r'W(\d+)_', path.name).group(1))
        if args.weeks and week not in args.weeks:
            continue
        if args.execute:
            execute(path)
        results.append(validate(path))
    print(json.dumps({'variant': VARIANT, 'notebooks': results}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
