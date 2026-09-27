from behave import given
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import ConfigReader

@given('the user is logged in as "{user_key}"')
def step_logged_in_as(context, user_key):
    login_page = LoginPage(context.driver)
    login_page.open()
    user = ConfigReader.get_user(user_key)
    login_page.login(user["username"], user["password"])
    context.inventory_page = InventoryPage(context.driver)