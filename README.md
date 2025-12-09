# auto-behave 🧪

Run behave feature files directly from VS Code's active tab with intelligent auto-completion!

## Features

✨ **Automatic Directory Detection** - Detects the active file in VS Code and runs behave from that directory  
⚡ **Tab Completion** - Auto-complete feature file names by pressing Tab  
🎯 **Simple Command** - Just type `feat feature_file.feature`  
🔄 **Fallback Support** - Uses current directory if VS Code detection fails  

## Installation

### 1. Install the package

```bash
pip install -e .
```

### 2. Enable tab completion

#### For PowerShell (Windows)
Add this to your PowerShell profile:

```powershell
# Register argcomplete for auto-behave
Register-ArgumentCompleter -Native -CommandName auto-behave -ScriptBlock {
    param($wordToComplete, $commandAst, $cursorPosition)
    $env:_ARGCOMPLETE = 1
    $env:_ARGCOMPLETE_COMP_WORDBREAKS = ' '
    $env:COMP_LINE = $commandAst.ToString()
    $env:COMP_POINT = $cursorPosition
    auto-behave 2>&1 | ForEach-Object { $_ }
}
```

To find your PowerShell profile location, run:
```powershell
echo $PROFILE
```

#### For Bash (Linux/Mac)
Add this to your `~/.bashrc` or `~/.bash_profile`:

```bash
eval "$(register-python-argcomplete auto-behave)"
```

#### For Zsh (Linux/Mac)
Add this to your `~/.zshrc`:

```bash
eval "$(register-python-argcomplete auto-behave)"
```

## Usage

### Basic Usage

```bash
# Run a feature file (auto-detects directory from VS Code active tab)
feat my_feature.feature
```

### With Tab Completion

1. Type `feat ` 
2. Press `Tab` to see available feature files
3. Start typing the file name and press `Tab` again to auto-complete

### With Behave Arguments

```bash
# Run with tags
auto-behave my_feature.feature --tags=@smoke

# Run with specific scenario
auto-behave my_feature.feature --name="User login"

# Dry run
auto-behave my_feature.feature --dry-run
```

### Specify Custom Directory

```bash
# Use a specific directory instead of auto-detection
auto-behave my_feature.feature -d /path/to/features
```

## How It Works

1. **Detects Active File**: When you run `feat`, it tries to detect which file is currently active in VS Code
2. **Finds Directory**: It extracts the directory path of the active file
3. **Changes Directory**: Automatically `cd`s to that directory
4. **Runs Behave**: Executes `behave feature_file.feature` in that directory
5. **Returns**: Changes back to your original directory

## Requirements

- Python 3.6+
- behave (for running tests)
- argcomplete (for tab completion)
- VS Code (optional, falls back to current directory)

## Troubleshooting

### "behave command not found"
Install behave:
```bash
pip install behave
```

### Tab completion not working
Make sure you:
1. Installed argcomplete: `pip install argcomplete`
2. Activated global completion: `activate-global-python-argcomplete --user`
3. Restarted your shell or ran `source ~/.bashrc` (or equivalent)

### VS Code active file not detected
The tool will automatically fall back to using your current working directory. You can also specify a directory manually with the `-d` flag.

## Development

### Install in development mode

```bash
pip install -e .
```

### Run tests

```bash
# Add tests here when created
pytest
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
