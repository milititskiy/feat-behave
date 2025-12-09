"""
Command-line interface for auto-behave
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path
import argcomplete
from argcomplete.completers import FilesCompleter

from .vscode_utils import get_active_file_from_vscode, get_current_working_directory


def find_feature_files(directory):
    """
    Find all .feature files in the given directory and subdirectories.
    """
    feature_files = []
    dir_path = Path(directory)
    
    if dir_path.exists() and dir_path.is_dir():
        # Search for .feature files recursively
        feature_files = list(dir_path.rglob('*.feature'))
        # Convert to relative paths for easier reading
        feature_files = [str(f.relative_to(dir_path)) for f in feature_files]
    
    return feature_files


class FeatureFileCompleter:
    """
    Custom completer for feature files based on the active VS Code tab directory.
    """
    def __call__(self, prefix, **kwargs):
        # Get the directory from VS Code active file or current directory
        active_file = get_active_file_from_vscode()
        
        if active_file:
            base_dir = os.path.dirname(active_file)
        else:
            base_dir = get_current_working_directory()
        
        # Find all feature files in the directory
        feature_files = find_feature_files(base_dir)
        
        # Filter based on the prefix
        matching_files = [f for f in feature_files if f.startswith(prefix)]
        
        return matching_files


def run_behave(feature_file, base_directory, extra_args=None):
    """
    Run behave command with the specified feature file.
    
    Args:
        feature_file: Name of the feature file to run
        base_directory: Directory where the feature file is located
        extra_args: Additional arguments to pass to behave
    """
    # Change to the base directory
    original_dir = os.getcwd()
    
    try:
        os.chdir(base_directory)
        print(f"📂 Changed directory to: {base_directory}")
        print(f"🧪 Running: behave {feature_file}")
        print("-" * 60)
        
        # Build the behave command
        cmd = ['behave', feature_file]
        if extra_args:
            cmd.extend(extra_args)
        
        # Run behave
        result = subprocess.run(cmd, shell=True)
        
        return result.returncode
        
    except FileNotFoundError:
        print("❌ Error: 'behave' command not found. Please install behave:")
        print("   pip install behave")
        return 1
    except Exception as e:
        print(f"❌ Error running behave: {e}")
        return 1
    finally:
        # Change back to original directory
        os.chdir(original_dir)


def main():
    """
    Main entry point for the auto-behave CLI.
    """
    parser = argparse.ArgumentParser(
        description='Run behave feature files from VS Code active tab',
        epilog='Example: auto-behave my_feature.feature'
    )
    
    parser.add_argument(
        'feature_file',
        help='Name of the feature file to run (supports tab completion)'
    ).completer = FeatureFileCompleter()
    
    parser.add_argument(
        '-d', '--directory',
        help='Base directory to search for feature file (default: auto-detect from VS Code)',
        default=None
    )
    
    parser.add_argument(
        'extra_args',
        nargs=argparse.REMAINDER,
        help='Additional arguments to pass to behave'
    )
    
    # Enable argcomplete
    argcomplete.autocomplete(parser)
    
    args = parser.parse_args()
    
    # Determine the base directory
    if args.directory:
        base_dir = args.directory
        print(f"📁 Using specified directory: {base_dir}")
    else:
        # Try to get active file from VS Code
        active_file = get_active_file_from_vscode()
        
        if active_file:
            base_dir = os.path.dirname(active_file)
            print(f"✅ Detected active file in VS Code: {active_file}")
            print(f"📁 Using directory: {base_dir}")
        else:
            # Fallback to current working directory
            base_dir = get_current_working_directory()
            print(f"⚠️  Could not detect VS Code active file")
            print(f"📁 Using current directory: {base_dir}")
    
    # Check if base directory exists
    if not os.path.exists(base_dir):
        print(f"❌ Error: Directory does not exist: {base_dir}")
        return 1
    
    # Check if feature file exists
    feature_path = os.path.join(base_dir, args.feature_file)
    if not os.path.exists(feature_path):
        print(f"❌ Error: Feature file not found: {feature_path}")
        print(f"\nAvailable feature files in {base_dir}:")
        feature_files = find_feature_files(base_dir)
        if feature_files:
            for f in feature_files[:10]:  # Show first 10
                print(f"  - {f}")
        else:
            print("  (none found)")
        return 1
    
    # Run behave
    return run_behave(args.feature_file, base_dir, args.extra_args)


if __name__ == '__main__':
    sys.exit(main())
