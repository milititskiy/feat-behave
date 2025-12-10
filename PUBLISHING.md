# 📦 Publishing feat-behave to PyPI

This guide shows you how to publish your package to PyPI so anyone can install it with `pip install feat-behave`.

## Prerequisites

1. **Create a PyPI account**: https://pypi.org/account/register/
2. **Create a TestPyPI account** (for testing): https://test.pypi.org/account/register/

## Step 1: Install Build Tools

```powershell
pip install --upgrade build twine
```

## Step 2: Update Package Information

Edit `setup.py` and update these fields:
- `author="Your Name"` → Your actual name
- `author_email="your.email@example.com"` → Your email
- `url="https://github.com/yourusername/feat-behave"` → Your GitHub repo URL (if you have one)

## Step 3: Build the Package

```powershell
# Make sure you're in the project root directory
cd C:\Users\km250730\OneDrive - NCR Voyix\Desktop\run_feature_file_from_active_tab

# Build the distribution packages
python -m build
```

This creates two files in the `dist/` folder:
- `feat_behave-0.1.0-py3-none-any.whl` (wheel file)
- `feat-behave-0.1.0.tar.gz` (source distribution)

## Step 4: Test Upload to TestPyPI (Recommended)

Test your package on TestPyPI first:

```powershell
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*
```

When prompted:
- Username: Your TestPyPI username
- Password: Your TestPyPI password (or API token)

Then test installing from TestPyPI:

```powershell
pip install --index-url https://test.pypi.org/simple/ feat-behave
```

## Step 5: Upload to PyPI (Production)

Once you've tested and everything works:

```powershell
# Upload to PyPI
python -m twine upload dist/*
```

When prompted:
- Username: Your PyPI username
- Password: Your PyPI password (or API token)

## Step 6: Verify Installation

After publishing, anyone can install your package:

```powershell
pip install feat-behave
```

Then use it:

```powershell
feat sample.feature
```

## 🔐 Using API Tokens (Recommended)

Instead of using passwords, use API tokens for security:

### For PyPI:
1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Use `__token__` as username
4. Use the token (including `pypi-` prefix) as password

### For TestPyPI:
1. Go to https://test.pypi.org/manage/account/token/
2. Create a new API token
3. Use `__token__` as username
4. Use the token as password

### Save Credentials (Optional)

Create `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YourActualTokenHere

[testpypi]
username = __token__
password = pypi-YourTestPyPITokenHere
```

## 📋 Checklist Before Publishing

- [ ] Updated `author` and `author_email` in `setup.py`
- [ ] Updated `url` in `setup.py` (GitHub repo if available)
- [ ] Updated version number if republishing
- [ ] Tested locally with `pip install -e .`
- [ ] README.md is clear and complete
- [ ] LICENSE file is included
- [ ] Tested on TestPyPI first
- [ ] No sensitive information in code

## 🔄 Updating Your Package

When you make changes and want to release a new version:

1. **Update version** in `setup.py`:
   ```python
   version="0.1.1",  # Increment version
   ```

2. **Rebuild**:
   ```powershell
   # Remove old builds
   Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
   
   # Build new version
   python -m build
   ```

3. **Upload**:
   ```powershell
   python -m twine upload dist/*
   ```

## 📝 Version Numbering

Follow semantic versioning (MAJOR.MINOR.PATCH):
- **0.1.0** → Initial release
- **0.1.1** → Bug fixes
- **0.2.0** → New features (backward compatible)
- **1.0.0** → First stable release
- **2.0.0** → Breaking changes

## ⚠️ Important Notes

1. **Package name must be unique**: `feat-behave` must not already exist on PyPI
   - Check: https://pypi.org/project/feat-behave/
   - If taken, choose a different name like `feat-runner`, `behave-feat`, etc.

2. **You can't delete packages**: Once uploaded to PyPI, you can only "yank" versions, not delete them

3. **Can't reuse version numbers**: Each upload must have a unique version number

## 🎯 Quick Reference

```powershell
# Install tools
pip install --upgrade build twine

# Build package
python -m build

# Test upload (TestPyPI)
python -m twine upload --repository testpypi dist/*

# Production upload (PyPI)
python -m twine upload dist/*

# Install your package
pip install feat-behave
```

## macOS / Linux (zsh/bash) commands

If you're on macOS or Linux with `zsh` or `bash`, use these commands (replace Windows PowerShell examples above):

```bash
# Install build tools
python -m pip install --upgrade build twine

# Clean previous builds
rm -rf dist build *.egg-info

# Build the package
python -m build

# Test upload to TestPyPI (recommended)
python -m twine upload --repository testpypi dist/*

# Production upload to PyPI
python -m twine upload dist/*
```

## CI: Publish from GitHub Actions

You can automate releases by creating a Git tag and pushing it to GitHub. The included workflow at `.github/workflows/publish.yml` listens for tags named like `v1.2.3` and will build and upload the `dist/` artifacts to PyPI.

Steps:

- Create a PyPI API token at https://pypi.org/manage/account/token/ and copy it.
- In your GitHub repo, go to `Settings -> Secrets -> Actions` and add a secret named `PYPI_API_TOKEN` with the token value.
- Locally, create a tag and push it:

```bash
# Update version in setup.py
git add setup.py
git commit -m "Bump version to v1.2.3"
git tag v1.2.3
git push origin v1.2.3
```

The workflow will run and publish the package to PyPI using the token stored in `PYPI_API_TOKEN`.

Notes:
- The workflow uses `TWINE_USERNAME=__token__` and `TWINE_PASSWORD` from `secrets.PYPI_API_TOKEN`.
- Make sure the `name` and `version` in `setup.py` are correct and unique on PyPI.

## 🔗 Useful Links

- **PyPI**: https://pypi.org/
- **TestPyPI**: https://test.pypi.org/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Documentation**: https://twine.readthedocs.io/

---

**After publishing, users can install with:**

```powershell
pip install feat-behave
```

**And use with:**

```powershell
feat sample.feature
```

🎉 **That's it! Your package is now available worldwide!**
