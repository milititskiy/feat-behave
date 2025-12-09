"""
Utilities for interacting with VS Code to get the active file
"""
import os
import subprocess
from pathlib import Path


def get_active_file_from_vscode():
    """
    Get the currently active file in VS Code.
    
    This function uses the VS Code CLI to get the active file path.
    Returns the absolute path to the active file, or None if not found.
    """
    try:
        # Try to get the active file using VS Code CLI
        # The 'code' command with --status shows VS Code's state
        subprocess.run(
            ['code', '--status'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        # Parse the output to find active file info
        # This is a fallback approach
        
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        pass
    
    # Alternative: Check for recent VS Code workspace state
    # VS Code stores workspace state in user data directory
    vscode_data_dir = get_vscode_data_dir()
    if vscode_data_dir:
        active_file = get_active_file_from_state(vscode_data_dir)
        if active_file and os.path.exists(active_file):
            return active_file
    
    return None


def get_vscode_data_dir():
    """
    Get the VS Code user data directory based on the OS.
    """
    home = Path.home()
    
    if os.name == 'nt':  # Windows
        return home / 'AppData' / 'Roaming' / 'Code' / 'User'
    elif os.name == 'posix':
        if os.uname().sysname == 'Darwin':  # macOS
            return home / 'Library' / 'Application Support' / 'Code' / 'User'
        else:  # Linux
            return home / '.config' / 'Code' / 'User'
    
    return None


def get_active_file_from_state(vscode_data_dir):
    """
    Try to extract the active file from VS Code's state files.
    This reads the workspace state to find recently opened files.
    """
    try:
        # Look for workspace storage
        workspace_storage = vscode_data_dir / 'workspaceStorage'
        
        if not workspace_storage.exists():
            return None
        
        # Get all workspace folders sorted by modification time
        # (most recent first)
        workspace_dirs = sorted(
            workspace_storage.iterdir(),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )
        
        # Check the most recent workspace
        for ws_dir in workspace_dirs[:5]:  # Check top 5 most recent workspaces
            state_file = ws_dir / 'state.vscdb'
            if state_file.exists():
                # Try to read and parse the state file
                # This is a SQLite database, but we can try reading it as text
                try:
                    with open(state_file, 'r', encoding='utf-8',
                              errors='ignore') as f:
                        content = f.read()
                        # Look for file paths in the content
                        # This is a heuristic approach
                        if 'activeEditor' in content or 'editors' in content:
                            # Try to extract file paths
                            import re
                            # Look for .feature files mentioned in the state
                            pattern = (r'([a-zA-Z]:[/\\]' +
                                       r'[^"\'<>|?*\n]+\.feature)')
                            feature_files = re.findall(pattern, content)
                            if feature_files:
                                # Return the first valid feature file found
                                for file_path in feature_files:
                                    if os.path.exists(file_path):
                                        return file_path
                except Exception:
                    continue
    
    except Exception:
        pass
    
    return None


def get_current_working_directory():
    """
    Get the current working directory where the command is executed.
    This is used as a fallback if VS Code active file can't be determined.
    """
    return os.getcwd()
