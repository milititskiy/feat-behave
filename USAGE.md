# 🎯 auto-behave - Quick Usage Guide

## Installation

Run the installation script:

```powershell
.\install.ps1
```

Or manually:

```powershell
pip install -e .
pip install behave argcomplete
```

## Basic Usage

### 1. Open a feature file in VS Code

Open any `.feature` file in VS Code as your active tab.

### 2. Run the feature file

```powershell
auto-behave filename.feature
```

The tool will:
- ✅ Detect the active file's directory
- ✅ Change to that directory automatically
- ✅ Run `behave filename.feature`
- ✅ Show you the results

## Examples

### Test with the included sample

1. Open `examples/sample.feature` in VS Code
2. Run:
   ```powershell
   auto-behave sample.feature
   ```

### With Tab Completion

1. Type: `auto-behave ` (with a space)
2. Press **Tab** - you'll see available `.feature` files
3. Start typing the filename and press **Tab** again to complete

### With Behave Options

```powershell
# Run only scenarios with @smoke tag
auto-behave sample.feature --tags=@smoke

# Run only scenarios with @regression tag
auto-behave sample.feature --tags=@regression

# Run with verbose output
auto-behave sample.feature --verbose

# Dry run (don't execute, just show what would run)
auto-behave sample.feature --dry-run

# Run specific scenario by name
auto-behave sample.feature --name="Successful login"
```

### Specify Custom Directory

If VS Code detection doesn't work, specify the directory:

```powershell
auto-behave sample.feature -d C:\path\to\features
```

## How It Works

```
You type:        auto-behave login.feature
                           ↓
                 Detects active tab in VS Code
                           ↓
                 Finds: C:\projects\tests\features\login.feature
                           ↓
                 Changes to: C:\projects\tests\features\
                           ↓
                 Runs: behave login.feature
                           ↓
                 Shows results in your terminal
```

## Common Workflows

### Workflow 1: Quick Test While Editing

1. Edit your feature file in VS Code
2. Save it (Ctrl+S)
3. Switch to terminal (Ctrl+`)
4. Type: `auto-behave [Tab]` to see available files
5. Select your file and press Enter

### Workflow 2: Run Specific Tags

```powershell
# Run all smoke tests
auto-behave my.feature --tags=@smoke

# Run everything except @wip (work in progress)
auto-behave my.feature --tags=~@wip
```

### Workflow 3: Debug Mode

```powershell
# Run with verbose output for debugging
auto-behave my.feature --verbose --no-capture
```

## Troubleshooting

### "auto-behave is not recognized"

**Solution:** Restart your terminal after installation.

### "behave is not recognized"

**Solution:** Install behave:
```powershell
pip install behave
```

### Tab completion not working

**Solution:** 
1. Make sure you added the completion script to your PowerShell profile
2. Restart your terminal
3. Test: type `auto-behave ` and press Tab

### VS Code active file not detected

**Solution:** The tool automatically falls back to the current directory. Make sure you're in the right directory, or use the `-d` flag:
```powershell
cd C:\path\to\your\features
auto-behave myfile.feature
```

### Feature file not found

**Solution:** Check that:
1. The feature file name is correct (case-sensitive on some systems)
2. You're in the correct directory
3. The file has a `.feature` extension

## Tips & Tricks

### Tip 1: Alias for Speed

Add to your PowerShell profile for even faster access:

```powershell
Set-Alias ab auto-behave
```

Then use: `ab myfile.feature`

### Tip 2: Create a Test Runner Script

Create `run-tests.ps1`:

```powershell
# Run all smoke tests
auto-behave feature1.feature --tags=@smoke
auto-behave feature2.feature --tags=@smoke
auto-behave feature3.feature --tags=@smoke
```

### Tip 3: Integration with VS Code Tasks

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Current Feature",
            "type": "shell",
            "command": "auto-behave ${fileBasename}",
            "group": "test",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        }
    ]
}
```

Press `Ctrl+Shift+P`, type "Run Task", select "Run Current Feature"!

## Need More Help?

- See `README.md` for detailed documentation
- See `INSTALL.md` for installation details
- Check the `examples/` folder for sample feature files

## Uninstall

```powershell
pip uninstall auto-behave
```

---

**Happy Testing! 🧪✨**
