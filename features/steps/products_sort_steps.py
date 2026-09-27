from behave import when, then

SORT_OPTION_MAP = {
    "Price (low to high)": "lohi",
    "Price (high to low)": "hilo",
    "Name (A to Z)": "az",
    "Name (Z to A)": "za",
}

@when('the user sort product by "{option_lable}"')
def step_sort_product(context, option_lable):
    option_value = SORT_OPTION_MAP[option_lable]
    context.inventory_page.sort_product(option_value)

@then('the products should be listed in ascending price order')
def step_verify_ascending_order(context):
    price = context.inventory_page.get_product_price()
    assert price == sorted(price), f"Price not in ascending order: {price}"

@then('the products should be listed in descending price order')
def step_verify_descending_order(context):
    price = context.inventory_page.get_product_price()
    assert price == sorted(price, reverse=True), f"Price not in descending order: {price}"

@then('the products should be listed as a to z')
def step_verify_atoz(context):
    name = context.inventory_page.get_product_names()
    assert name == sorted(name), f"Not sorted in A to Z"

@then('the products should be listed as z to a')
def step_verify_ztoa(context):
    name = context.inventory_page.get_product_names()
    assert name == sorted(name, reverse= True), f"Not sorted in Z to A"