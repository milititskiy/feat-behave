# Build script for feat-behave package
# This prepares the package for PyPI upload

Write-Host "Building feat-behave package..." -ForegroundColor Cyan
Write-Host ""

# Step 1: Install build tools
Write-Host "Step 1: Installing/upgrading build tools..." -ForegroundColor Yellow
pip install --upgrade build twine

Write-Host ""
Write-Host "Step 2: Cleaning old builds..." -ForegroundColor Yellow
# Remove old build artifacts
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "Step 3: Building distribution packages..." -ForegroundColor Yellow
# Build the package
python -m build

Write-Host ""
Write-Host "Build complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Generated files in dist/:" -ForegroundColor Cyan
Get-ChildItem dist

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Test upload to TestPyPI:" -ForegroundColor White
Write-Host "   python -m twine upload --repository testpypi dist/*" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Upload to PyPI:" -ForegroundColor White
Write-Host "   python -m twine upload dist/*" -ForegroundColor Gray
Write-Host ""
Write-Host "For detailed instructions, see PUBLISHING.md" -ForegroundColor Cyan
