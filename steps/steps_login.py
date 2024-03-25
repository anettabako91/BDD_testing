from behave import *


@given('I am on the login page')
def step_impl(context):
    # pass  # nu face nimic, doar ne ajuta sa scapam de eroare cand cream ceva nou
    context.login_page.navigate_to_login_page()


@when('I enter "{email}" in email field')  # aici practic ii dam un nume de variabila la email.important sa fie peste tot trecut la fel
def step_impl(context, email):
    context.login_page.enter_email(email)


@when('I enter "{passw}" in password field')
def step_impl(context, passw):
    context.login_page.enter_password(passw)


@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.login_page.get_error_message()
    expected_error_message = 'Login was unsuccessful. Please correct the errors and try again.'
    assert expected_error_message in actual_error_message


#
# @when('I enter a wrong format email')
# def step_impl(context):
#     context.login_page.enter_wrong_format_email()

@when('I press the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I should see an error for email')
def step_impl(context):
    actual_error_message = context.login_page.get_email_error()
    expected_error_message = "Wrong email"
    assert expected_error_message in actual_error_message
