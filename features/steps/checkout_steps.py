from behave import given, when, then
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@when('the user adds "{product_name}" to the cart')
def step_add_product(context, product_name):
    context.inventory_page.add_product_to_cart(product_name)

@then('the cart badge should show "{count}" item')
def step_verify_cart_count(context, count):
    actual = context.inventory_page.get_cart_count()
    assert actual == int(count), f"Expected cart {count}, get {actual}"

@when('the user adds the following products to cart')
def step_add_multiple_products(context):
    for row in context.table:
        context.inventory_page.add_product_to_cart(row["product_name"])

@given('the user has added "{product_name}" to cart')
def step_pre_added_producrs(context, product_name):
    context.inventory_page.add_product_to_cart(product_name)

@when('the user opens the cart')
def step_open_cart(context):
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.driver)

@when("removes the first item from the cart")
def step_remove_first_item(context):
    context.cart_page.remove_first_item()

@then('the cart should be empty')
def step_varify_empty_cart(context):
    items = context.cart_page.get_cart_item_name()
    assert len(items) == 0, f"Cart should be empty, found {items}"

@when('proceeds to checkout')
def step_proceeds_to_checkout(context):
    context.cart_page.proceed_to_checkout()
    context.checkout_page = CheckoutPage(context.driver)

@when('fills the checkout info "{first_name:MaybeEmpty}" "{last_name:MaybeEmpty}" "{zip_code:MaybeEmpty}"')
def step_fill_checkout_info(context, first_name, last_name, zip_code):
    context.checkout_page.fill_checkout_info(first_name, last_name, zip_code)

@when('finish the checkout')
def step_finish_checkout(context):
    context.checkout_page.finish_checkout()

@then('the user should see the order confirmation message "{message}"')
def step_verify_confirmation(context, message):
    actual = context.checkout_page.get_completion_message()
    assert message in actual, f"Expected '{message}' but got '{actual}'"

@then('the user should see the checkout error message')
def step_verify_error_message(context):
    error = context.checkout_page.get_error_message()
    assert error, "Expected a checkout validation error message to be displayed"