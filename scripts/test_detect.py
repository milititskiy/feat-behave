"""Simple test script to exercise VS Code active-file detection and listing.

Run from project root:

    python3 scripts/test_detect.py

It will print:
- current working directory
- detected active file (if any)
- feature files found in the detected directory and in `examples/`
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from auto_behave.vscode_utils import get_active_file_from_vscode, get_current_working_directory
from auto_behave.cli import find_feature_files


def main():
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")

    active = get_active_file_from_vscode()
    print(f"Detected active file from VS Code: {active}")

    if active:
        base = os.path.dirname(active)
        print(f"Feature files under detected directory ({base}):")
        for f in find_feature_files(base):
            print(f"  - {f}")
    else:
        print("No active file detected. Falling back to current working directory for listing examples.")

    examples_dir = os.path.join(os.path.dirname(__file__), '..', 'examples')
    examples_dir = os.path.normpath(examples_dir)
    print(f"Listing .feature files under examples directory: {examples_dir}")
    for f in find_feature_files(examples_dir):
        print(f"  - {f}")

    examples2_dir = os.path.join(os.path.dirname(__file__), '..', 'examples_2')
    examples2_dir = os.path.normpath(examples2_dir)
    print(f"Listing .feature files under examples_2 directory: {examples2_dir}")
    for f in find_feature_files(examples2_dir):
        print(f"  - {f}")


if __name__ == '__main__':
    main()
