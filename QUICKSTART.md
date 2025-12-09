# 🚀 Getting Started with auto-behave

Welcome! This guide will get you up and running in 5 minutes.

## What is auto-behave?

`auto-behave` is a command-line tool that makes running Behave feature files from VS Code super easy. Just type `auto-behave myfile.feature` and it automatically:

1. 🔍 Detects which file is open in VS Code
2. 📂 Finds the directory where that file lives
3. 🏃 Changes to that directory
4. ✅ Runs `behave myfile.feature`
5. ⚡ Supports Tab completion for file names!

## Quick Start (3 Steps)

### Step 1: Install

Open PowerShell in this directory and run:

```powershell
.\install.ps1
```

This will install:
- ✅ The `auto-behave` command
- ✅ Behave (the BDD framework)
- ✅ Tab completion support

### Step 2: Test It

Open the sample feature file in VS Code:
- Open: `examples/sample.feature`

Then run in your terminal:

```powershell
auto-behave sample.feature
```

You should see the tests run! 🎉

### Step 3: Enable Tab Completion (Optional)

1. Open your PowerShell profile:
   ```powershell
   notepad $PROFILE
   ```

2. Add this code:
   ```powershell
   Register-ArgumentCompleter -Native -CommandName auto-behave -ScriptBlock {
       param($wordToComplete, $commandAst, $cursorPosition)
       $env:_ARGCOMPLETE = 1
       $env:_ARGCOMPLETE_COMP_WORDBREAKS = ' '
       $env:COMP_LINE = $commandAst.ToString()
       $env:COMP_POINT = $cursorPosition
       auto-behave 2>&1 | ForEach-Object { $_ }
   }
   ```

3. Restart PowerShell

4. Test: Type `auto-behave ` and press **Tab**!

## Usage

```powershell
# Basic usage
auto-behave myfile.feature

# With behave options
auto-behave myfile.feature --tags=@smoke
auto-behave myfile.feature --verbose
auto-behave myfile.feature --dry-run

# Custom directory
auto-behave myfile.feature -d C:\path\to\features
```

## Need Help?

📖 **Detailed Documentation:**
- `README.md` - Full documentation
- `INSTALL.md` - Installation details
- `USAGE.md` - Usage examples and tips
- `PROJECT.md` - Project structure

❓ **Common Issues:**
- Command not found? → Restart your terminal
- Behave not found? → Run `pip install behave`
- Tab completion not working? → Complete Step 3 above

## What's Next?

1. **Create your own feature files** in your project
2. **Open them in VS Code**
3. **Run with** `auto-behave yourfile.feature`
4. **Enjoy fast BDD testing!** 🚀

---

## Project Structure

```
📁 run_feature_file_from_active_tab/
  📄 install.ps1          ← Run this first!
  📄 QUICKSTART.md        ← You are here
  📄 README.md            ← Full documentation
  📄 USAGE.md             ← Usage guide
  📁 auto_behave/         ← Main package code
  📁 examples/            ← Sample feature files to test
```

---

**Happy Testing! 🧪✨**

Got questions? Check the documentation files listed above!
