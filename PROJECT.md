# 📦 Project Structure

```
auto-behave/
│
├── auto_behave/              # Main package directory
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # Command-line interface & main logic
│   └── vscode_utils.py      # VS Code integration utilities
│
├── examples/                 # Example feature files for testing
│   ├── sample.feature       # Sample BDD feature file
│   └── steps/
│       └── sample_steps.py  # Step definitions for sample.feature
│
├── setup.py                  # Package installation configuration
├── requirements.txt          # Python dependencies
├── install.ps1              # Quick installation script (Windows)
│
├── README.md                # Main documentation
├── INSTALL.md               # Detailed installation guide
├── USAGE.md                 # Usage examples and tips
├── LICENSE                  # MIT License
└── .gitignore              # Git ignore patterns

```

## Key Components

### 1. **cli.py** - The Heart of the Tool
- Command-line argument parsing
- Tab completion setup
- Behave execution logic
- Feature file discovery

### 2. **vscode_utils.py** - VS Code Integration
- Detects active file in VS Code
- Reads VS Code workspace state
- Fallback to current directory

### 3. **setup.py** - Package Configuration
- Defines package metadata
- Sets up the `auto-behave` command
- Manages dependencies

## How to Use This Project

### For Installation:
```powershell
.\install.ps1
```

### For Development:
```powershell
pip install -e .  # Install in editable mode
```

### For Testing:
```powershell
# Open examples/sample.feature in VS Code, then:
auto-behave sample.feature
```

## Features Implemented

✅ **Command-line tool** - Installed as `auto-behave` command
✅ **VS Code detection** - Automatically finds active file
✅ **Directory navigation** - Auto-changes to feature file directory
✅ **Tab completion** - Auto-complete feature file names
✅ **Behave integration** - Seamless behave execution
✅ **Error handling** - Graceful fallbacks and helpful messages
✅ **Cross-directory support** - Works with any directory structure

## Commands Available

- `auto-behave <file>.feature` - Run a feature file
- `auto-behave <file>.feature --tags=@tag` - Run with tags
- `auto-behave <file>.feature -d <dir>` - Specify directory
- `auto-behave --help` - Show help

## Next Steps for Enhancement

Some ideas for future improvements:
1. Support for parallel execution
2. HTML report generation
3. Integration with CI/CD pipelines
4. Configuration file support (.auto-behave.yml)
5. VS Code extension version
6. Support for other BDD frameworks (Cucumber, pytest-bdd)

## Tech Stack

- **Python 3.6+** - Core language
- **argcomplete** - Tab completion
- **behave** - BDD framework
- **VS Code** - Editor integration

---

**Created with ❤️ for easier BDD testing!**
