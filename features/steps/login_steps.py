from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import ConfigReader

@given('the user is on login page')
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('the user logs in as "{user_key}"')
def step_login_as_user(context, user_key):
    user = ConfigReader.get_user(user_key)
    context.login_page.login(user["username"], user["password"])

@given('the user logs in as "{user_key}"')
def step_login_as_user(context, user_key):
    user = ConfigReader.get_user(user_key)
    context.login_page.login(user["username"], user["password"])

@then('the user land on product page')
def step_verify_user_is_on_product_page(context):
    context.inventory_page = InventoryPage(context.driver)
    assert context.inventory_page.is_loaded(), "Expected to land on the Products page after login"

@when('the user logs in with invalid creds "{username:MaybeEmpty}" and password "{password:MaybeEmpty}"')
def step_login_with_creds(context, username, password):
    context.login_page.login(username, password)

@then('the user should see the error message "{message}"')
def step_verify_specific_error_message(context, message):
    actual = context.login_page.get_error_message()
    assert message in actual, f"Expected error '{message}' but got '{actual}'"

@then('the user should see the error message')
def step_verify_generic_error_message(context):
    assert context.login_page.is_error_displayed(), "Expected an error message to be displayed"