from selenium.webdriver.common.by import By 
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CONTINUE_SHOP_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_item_name(self):
        elemnets = self.find_all_immediate(self.CART_ITEM_NAME)
        names = []
        for item in elemnets:
                    names.append(item.text)
        return names

    def remove_first_item(self):
           self.click(self.REMOVE_BUTTON)

    def proceed_to_checkout(self):
           self.click(self.CHECKOUT_BUTTON)

    def back_to_inventory_page(self):
           self.click(self.CONTINUE_SHOP_BUTTON)