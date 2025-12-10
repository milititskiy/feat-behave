from behave import given, when, then


@given('I have a feature in another directory')
def step_impl_given(context):
    # No setup required for this example
    pass


@when('I run detection')
def step_impl_when(context):
    # Simulate action
    pass


@then('the detector should be able to find it')
def step_impl_then(context):
    # Simple assertion placeholder
    assert True
