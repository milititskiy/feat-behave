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
        # The 'code' command with --status prints state info we can parse
        result = subprocess.run(
            ['code', '--status'],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.stdout:
            import re
            # Look for file:// URLs or absolute paths in the output
            # Examples: file:///Users/you/project/file.feature or /Users/you/project/file.feature
            patterns = [r'file://[^\s\)\]\']+\.feature', r'(/[^\s\)\]\']+\.feature)']
            for pat in patterns:
                m = re.search(pat, result.stdout)
                if m:
                    path = m.group(0)
                    # strip file:// if present
                    if path.startswith('file://'):
                        from urllib.parse import unquote, urlparse
                        parsed = urlparse(path)
                        path = unquote(parsed.path)

                    if os.path.exists(path):
                        return path
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

        # Get workspace folders sorted by modification time (most recent first)
        workspace_dirs = sorted(
            workspace_storage.iterdir(),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )

        import re
        # Patterns to capture Windows paths, Unix paths, and file:// URIs
        patterns = [
            r'([A-Za-z]:[/\\][^"\'<>|?*\n]+\.feature)',
            r'(/[^"\'<>|?*\n]+\.feature)',
            r'file://[^\s\)\]\']+\.feature'
        ]

        # Check the most recent workspaces and scan files within for traces
        for ws_dir in workspace_dirs[:10]:  # widen search to top 10
            # Walk files in the workspace storage directory (non-recursive depth-limited)
            try:
                for p in ws_dir.rglob('*'):
                    if p.is_file():
                        try:
                            # Read as binary and decode with latin1 to preserve bytes
                            with open(p, 'rb') as f:
                                raw = f.read()
                                try:
                                    text = raw.decode('utf-8', errors='ignore')
                                except Exception:
                                    text = raw.decode('latin1', errors='ignore')

                                for pat in patterns:
                                    matches = re.findall(pat, text)
                                    if matches:
                                        # matches may be tuples if groups used
                                        for m in matches:
                                            candidate = m if isinstance(m, str) else (m[0] if m else None)
                                            if not candidate:
                                                continue
                                            # strip file:// if present
                                            if candidate.startswith('file://'):
                                                from urllib.parse import unquote, urlparse
                                                parsed = urlparse(candidate)
                                                candidate = unquote(parsed.path)

                                            # Normalize tilde and such
                                            candidate = os.path.expanduser(candidate)
                                            if os.path.exists(candidate):
                                                return candidate
                        except Exception:
                            continue
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
