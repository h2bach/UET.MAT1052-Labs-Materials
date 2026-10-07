"""Validate the review notebooks; optionally execute each from a fresh kernel.

Run from any directory: python -X utf8 tools/verify_w05_w07.py [--execute]
The default run only reads notebooks, assets and Git history.
"""
from pathlib import Path
import argparse
import ast
import json
import re
import subprocess
import sys
import tempfile

import nbformat

BASE = Path(__file__).resolve().parents[1]
VARIANT = json.loads((BASE / 'NOTEBOOK_VARIANT.json').read_text(encoding='utf-8'))
BACKEND = VARIANT['backend']
BACKEND_MARKDOWN = {
    5: {'w05-001', 'w05-090'},
    6: {'473db095', '66f65aea'},
    7: {'4f43d6de', 'e3619f5f', 'b257227b'},
}
FILES = {
    5: 'W5_NenTangVaTinhToanXacSuat.ipynb',
    6: 'W6_PhanPhoiVaBienNgauNhien.ipynb',
    7: 'W7_KyVongPhuongSaiVaXapXiChuan.ipynb',
}
MODULES = {
    5: '05_probability', 6: '06_distributions_random_variables',
    7: '07_expectation_variance_normal',
}
W05_IDS = {
    'W05-Q01','W05-Q02','W05-Q03', 'W05-EX01','W05-EX02','W05-EX03',
    'W05-EX04','W05-EX05','W05-BT01','W05-BT02','W05-BT04','W05-BT05',
    'W05-BT07','W05-BT08','W05-CH01','W05-CASE01','W05-TH01','W05-TH03',
}
AUTHOR = 'ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET'

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def normalize_source(source):
    return source.replace('../datasets/', 'datasets/').replace('\r\n', '\n')

def validate(path, week):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    ids = [cell.id for cell in notebook.cells]
    require(len(ids) == len(set(ids)), f'{path.name}: duplicate cell IDs')
    markdown = '\n'.join(cell.source for cell in notebook.cells if cell.cell_type == 'markdown')
    page_count = {5:93, 6:80, 7:94}[week]
    source_pages = {p for cell in notebook.cells for p in cell.metadata.get('source_pages', [])}
    require(source_pages == set(range(1, page_count+1)),
            f'{path.name}: slide-page coverage differs')
    require(AUTHOR in markdown, f'{path.name}: missing author header')
    require(not any(char in markdown for char in ['\x08','\x0b','\x0c','\x00']),
            f'{path.name}: escaped LaTeX contains control characters')
    # Check the rendered HTML, because a valid notebook can still expose answers
    # outside a visually empty <details> block after Markdown sanitization.
    from nbconvert.filters import markdown2html
    for cell in notebook.cells:
        if cell.cell_type == 'markdown' and '<details' in cell.source:
            rendered = markdown2html(cell.source)
            blocks = re.findall(r'<details[^>]*>(.*?)</details>', rendered, flags=re.S)
            require(bool(blocks), f'{path.name}: lost collapsible answers at {cell.id}')
            for block in blocks:
                answer = re.sub(r'<summary[^>]*>.*?</summary>', '', block, flags=re.S)
                require(bool(re.sub(r'<[^>]+>', '', answer).strip()),
                        f'{path.name}: empty collapsible answer at {cell.id}')
    code_cells = [cell for cell in notebook.cells if cell.cell_type == 'code' and cell.source.strip()]
    for cell in code_cells:
        if BACKEND == 'matplotlib-plotly':
            require('plotnine' not in cell.source.lower(), f'{path.name}: wrong graphics backend')
        else:
            require(not re.search(r'(?:import|from)\s+(?:matplotlib|plotly|seaborn)\b', cell.source),
                    f'{path.name}: non-Plotnine graphics import at {cell.id}')
            require(not re.search(r'\b(?:plt|pio|go|px)\.', cell.source),
                    f'{path.name}: non-Plotnine graphics call at {cell.id}')
        require(cell.execution_count is not None, f'{path.name}: unexecuted code cell {cell.id}')
        # Ignore notebook magics while checking ordinary Python syntax.
        syntax_source = '\n'.join(line for line in cell.source.splitlines()
                                  if not line.lstrip().startswith(('%','!')))
        ast.parse(syntax_source)
        for output in cell.get('outputs', []):
            require(output.output_type != 'error', f'{path.name}: code error {cell.id}')
            if output.output_type == 'stream' and output.name == 'stderr':
                require(not output.text.strip(), f'{path.name}: stderr {cell.id}: {output.text}')
    images = []
    for cell in notebook.cells:
        if cell.cell_type != 'markdown':
            continue
        targets = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', cell.source)
        targets += re.findall(r'<img[^>]+src=[\"\x27]([^\"\x27]+)', cell.source)
        for target in targets:
            if target.startswith('attachment:'):
                require(target[11:] in cell.get('attachments', {}), f'{path.name}: missing attachment {target}')
            elif not target.startswith(('https://','http://','data:')):
                require((path.parent / target).is_file(), f'{path.name}: missing image {target}')
            images.append(target)
    source_ids = set(re.findall(r'W05-[A-Z]+\d+', markdown))
    if week == 5:
        require(source_ids == W05_IDS, f'{path.name}: exercise IDs differ: {source_ids ^ W05_IDS}')
    elif week == 6:
        examples = set(int(n) for n in re.findall(r'Ví dụ\s+(\d+)', markdown))
        require(set(range(1,22)) <= examples, f'{path.name}: missing examples {set(range(1,22))-examples}')
    else:
        examples = set(int(n) for n in re.findall(r'Ví dụ\s+(\d+)', markdown))
        exercises = set(int(n) for n in re.findall(r'Bài tập\s+(\d+)', markdown))
        require(set(range(1,16)) <= examples, f'{path.name}: missing examples {set(range(1,16))-examples}')
        require(set(range(1,11)) <= exercises, f'{path.name}: missing exercises {set(range(1,11))-exercises}')
    module = BASE.parent / MODULES[week] / 'notebook.ipynb'
    if module.is_file() and BACKEND == 'matplotlib-plotly':
        source = nbformat.read(module, as_version=4)
        require(len(source.cells) == len(notebook.cells), f'{path.name}: source/release cell count differs')
        for left, right in zip(source.cells, notebook.cells):
            require(left.cell_type == right.cell_type and normalize_source(left.source) == normalize_source(right.source),
                    f'{path.name}: source/release content differs at {right.id}')
    outputs = [o for cell in code_cells for o in cell.outputs]
    pngs = sum('image/png' in o.get('data', {}) for o in outputs)
    plotly = sum('application/vnd.plotly.v1+json' in o.get('data', {}) for o in outputs)
    require(pngs > 0, f'{path.name}: missing PNG figures')
    parity = None
    if BACKEND == 'matplotlib-plotly':
        require(plotly > 0, f'{path.name}: missing Plotly figures')
    else:
        code = '\n'.join(c.source for c in code_cells)
        require('import plotnine as p9' in code, f'{path.name}: missing Plotnine setup')
        require(plotly == 0, f'{path.name}: stale Plotly output')
        original = subprocess.run(['git','show',f"{VARIANT['original_content_commit']}:{path.name}"],
                                  cwd=BASE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if original.returncode == 0:
            baseline = nbformat.reads(original.stdout.decode('utf-8'), as_version=4)
            require([c.id for c in baseline.cells] == ids, f'{path.name}: cell IDs changed')
            for left, right in zip(baseline.cells, notebook.cells):
                require(left.cell_type == right.cell_type and {k:v for k,v in left.metadata.items() if k != 'execution'} == {k:v for k,v in right.metadata.items() if k != 'execution'},
                        f'{path.name}: source metadata changed at {right.id}')
                if right.cell_type == 'markdown' and right.id not in BACKEND_MARKDOWN[week]:
                    require(left.source == right.source, f'{path.name}: theory/exercise changed at {right.id}')
            parity = True
    return {'week': week, 'file':path.name, 'cells':len(notebook.cells),
            'code_cells':len(code_cells), 'png_outputs':pngs, 'plotly_outputs':plotly,
            'illustrations':len(images), 'slide_pages':page_count,
            'clean_execution': True, 'backend':BACKEND,
            'source_release_aligned':module.is_file() if BACKEND == 'matplotlib-plotly' else None,
            'theory_exercises_preserved':parity}

def check_preserved():
    baseline = '2b48b0175d1d94915a5c42f62437af7ad116d9ad'
    preserved = []
    output_only_changes = []
    old_files = ['W1_CauHoiVaDuLieu.ipynb','W2_TomTatDuLieu.ipynb',
                 'W3_NguPhapDoHoaVaDieuKienHoa.ipynb','W3_TFT_NguPhapDoHoaVaDieuKienHoa.ipynb',
                 'W3_TFT_GiaiThichTungCell.md','W4_TuongQuanVaHoiQuyTuyenTinh.ipynb']
    for name in old_files:
        original = subprocess.run(['git','show',f'{baseline}:{name}'], cwd=BASE,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if original.returncode != 0:
            # A shallow download/clone may not include the preserved baseline commit.
            return {'baseline_available':False, 'files_checked':[]}
        current = (BASE/name).read_bytes().replace(b'\r\n',b'\n')
        if original.stdout.replace(b'\r\n',b'\n') != current:
            # W4 was saved externally during authoring. Keep that save, and
            # accept only execution-count/output changes, never content edits.
            require(name == 'W4_TuongQuanVaHoiQuyTuyenTinh.ipynb',
                    f'Existing file changed: {name}')
            before, after = json.loads(original.stdout), json.loads(current)
            for notebook in (before, after):
                for cell in notebook['cells']:
                    cell.pop('execution_count', None)
                    cell.pop('outputs', None)
            require(before == after, f'Existing notebook content changed: {name}')
            output_only_changes.append(name)
        preserved.append(name)
    return {'baseline_available':True,'files_checked':preserved,
            'execution_output_only_changes':output_only_changes}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='Run each notebook in a fresh kernel and save outputs')
    args = parser.parse_args()
    results = []
    for week, name in FILES.items():
        path = BASE/name
        if args.execute:
            from nbclient import NotebookClient
            notebook = nbformat.read(path, as_version=4)
            from jupyter_client import KernelManager
            from jupyter_client.kernelspec import KernelSpecManager
            with tempfile.TemporaryDirectory(prefix='xstk-kernel-') as kernel_dir:
                spec = Path(kernel_dir)/'xstk-active-python'
                spec.mkdir()
                (spec/'kernel.json').write_text(json.dumps({
                    'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
                    'display_name':'XSTK active Python','language':'python',
                }), encoding='utf-8')
                manager = KernelManager(kernel_name='xstk-active-python',
                    kernel_spec_manager=KernelSpecManager(kernel_dirs=[kernel_dir]))
                try:
                    NotebookClient(notebook, km=manager, timeout=240,
                                   resources={'metadata':{'path':str(BASE)}}).execute()
                finally:
                    if manager.has_kernel:
                        manager.shutdown_kernel(now=True)
            nbformat.write(notebook, path)
        results.append(validate(path, week))
    print(json.dumps({'notebooks':results, 'existing_materials':check_preserved()}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
