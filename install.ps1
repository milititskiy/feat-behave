# Quick Start Script for auto-behave
# Run this script to install and set up auto-behave

Write-Host "Installing auto-behave..." -ForegroundColor Cyan
Write-Host ""

# Install the package
Write-Host "Installing package in development mode..." -ForegroundColor Yellow
pip install -e .

# Install behave if not already installed
Write-Host ""
Write-Host "Installing behave..." -ForegroundColor Yellow
pip install behave

# Install argcomplete for tab completion
Write-Host ""
Write-Host "Installing argcomplete for tab completion..." -ForegroundColor Yellow
pip install argcomplete

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host ""

# Check if feat command is available
Write-Host "Verifying installation..." -ForegroundColor Cyan
try {
    $null = Get-Command feat -ErrorAction Stop
    Write-Host "'feat' command is available!" -ForegroundColor Green
} catch {
    Write-Host "Warning: 'feat' command not found. Try restarting your terminal." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. To enable tab completion, add the following to your PowerShell profile:"
Write-Host "   Run: notepad `$PROFILE" -ForegroundColor White
Write-Host ""
Write-Host "2. Add this code to the profile:" -ForegroundColor White
Write-Host ""
Write-Host "# Register argcomplete for feat command" -ForegroundColor Gray
Write-Host "Register-ArgumentCompleter -Native -CommandName feat -ScriptBlock {" -ForegroundColor Gray
Write-Host "    param(`$wordToComplete, `$commandAst, `$cursorPosition)" -ForegroundColor Gray
Write-Host "    `$env:_ARGCOMPLETE = 1" -ForegroundColor Gray
Write-Host "    `$env:_ARGCOMPLETE_COMP_WORDBREAKS = ' '" -ForegroundColor Gray
Write-Host "    `$env:COMP_LINE = `$commandAst.ToString()" -ForegroundColor Gray
Write-Host "    `$env:COMP_POINT = `$cursorPosition" -ForegroundColor Gray
Write-Host "    feat 2>&1 | ForEach-Object { `$_ }" -ForegroundColor Gray
Write-Host "}" -ForegroundColor Gray
Write-Host ""

Write-Host "3. Restart PowerShell or run: . `$PROFILE" -ForegroundColor White
Write-Host ""
Write-Host "4. Test it: feat [TAB]" -ForegroundColor White
Write-Host ""
Write-Host "For more information, see INSTALL.md" -ForegroundColor Cyan
Write-Host ""
