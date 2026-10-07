"""Compatibility entry point: verify weeks 5-7 using the current branch backend."""
import sys
from verify_notebooks import main

if __name__ == '__main__':
    main([*sys.argv[1:], '--weeks', '5', '6', '7'])
