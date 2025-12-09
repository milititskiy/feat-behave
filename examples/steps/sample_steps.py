"""
Sample step definitions for the sample.feature file
"""
from behave import given, when, then


@given('I am on the login page')
def step_impl(context):
    print("✅ Navigating to login page...")
    context.on_login_page = True


@when('I enter username "{username}"')
def step_impl(context, username):
    print(f"✅ Entering username: {username}")
    context.username = username


@when('I enter password "{password}"')
def step_impl(context, password):
    print(f"✅ Entering password: {'*' * len(password)}")
    context.password = password


@when('I click the login button')
def step_impl(context):
    print("✅ Clicking login button...")
    context.login_clicked = True


@then('I should be logged in successfully')
def step_impl(context):
    print("✅ Verifying successful login...")
    assert context.username == "testuser", "Username mismatch"
    assert context.password == "password123", "Password mismatch"
    print("✅ Login successful!")


@then('I should see an error message')
def step_impl(context):
    print("✅ Verifying error message is displayed...")
    assert context.username != "testuser", "Should have invalid username"
    print("✅ Error message displayed correctly!")
