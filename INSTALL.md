# Installation and Setup Guide for auto-behave

## Step-by-Step Installation

### 1. Install the package in development mode

Open your terminal in the project directory and run:

```powershell
pip install -e .
```

This will install the package and create the `auto-behave` command.

### 2. Install behave (if not already installed)

```powershell
pip install behave
```

### 3. Enable Tab Completion (Optional but Recommended)

#### For PowerShell:

1. First, install argcomplete globally:
```powershell
pip install argcomplete
```

2. Find your PowerShell profile location:
```powershell
echo $PROFILE
```

3. Open the profile file (create it if it doesn't exist):
```powershell
notepad $PROFILE
```

4. Add this line to the profile:
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

5. Restart PowerShell or reload the profile:
```powershell
. $PROFILE
```

## Testing the Installation

### 1. Create a test feature file

Create a folder structure for testing:

```powershell
mkdir test_features
cd test_features
```

Create a file named `login.feature`:

```gherkin
Feature: User Login
  As a user
  I want to log in to the application
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid username "testuser"
    And I enter valid password "password123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see a welcome message

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter invalid username "wronguser"
    And I enter invalid password "wrongpass"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page
```

### 2. Create a basic steps file

Create a folder `steps` inside `test_features`:

```powershell
mkdir steps
```

Create `test_features/steps/login_steps.py`:

```python
from behave import given, when, then

@given('I am on the login page')
def step_impl(context):
    print("Opening login page...")
    pass

@when('I enter valid username "{username}"')
def step_impl(context, username):
    print(f"Entering username: {username}")
    context.username = username

@when('I enter valid password "{password}"')
def step_impl(context, password):
    print(f"Entering password: {password}")
    context.password = password

@when('I enter invalid username "{username}"')
def step_impl(context, username):
    print(f"Entering invalid username: {username}")
    context.username = username

@when('I enter invalid password "{password}"')
def step_impl(context, password):
    print(f"Entering invalid password: {password}")
    context.password = password

@when('I click the login button')
def step_impl(context):
    print("Clicking login button...")
    pass

@then('I should be redirected to the dashboard')
def step_impl(context):
    print("Checking redirect to dashboard...")
    assert context.username == "testuser"

@then('I should see a welcome message')
def step_impl(context):
    print("Verifying welcome message...")
    pass

@then('I should see an error message')
def step_impl(context):
    print("Verifying error message...")
    pass

@then('I should remain on the login page')
def step_impl(context):
    print("Verifying still on login page...")
    pass
```

### 3. Test the auto-behave command

Open the `login.feature` file in VS Code, then run:

```powershell
auto-behave login.feature
```

You should see behave execute your feature file!

### 4. Test tab completion

Type this and press Tab after the space:

```powershell
auto-behave [TAB]
```

You should see `login.feature` appear as an option!

## Troubleshooting

### Error: "auto-behave" is not recognized

- Make sure you installed the package: `pip install -e .`
- Try closing and reopening your terminal
- Check if the Scripts folder is in your PATH

### Error: "behave" is not recognized

- Install behave: `pip install behave`

### Tab completion not working

- Make sure argcomplete is installed: `pip install argcomplete`
- Make sure you added the completion script to your PowerShell profile
- Restart your terminal after updating the profile

### VS Code active file not detected

- The tool will automatically fall back to the current directory
- Make sure the feature file is in the current directory or use `-d` flag:
  ```powershell
  auto-behave login.feature -d C:\path\to\features
  ```

## Usage Examples

```powershell
# Basic usage
auto-behave login.feature

# With behave tags
auto-behave login.feature --tags=@smoke

# With specific scenario name
auto-behave login.feature --name="Successful login"

# Dry run
auto-behave login.feature --dry-run

# Verbose output
auto-behave login.feature --verbose

# Custom directory
auto-behave login.feature -d C:\my\features
```

## Uninstalling

```powershell
pip uninstall auto-behave
```
