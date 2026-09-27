from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container") 

    def is_loaded(self):
        return self.is_visible(self.PAGE_TITLE) and self.get_text(self.PAGE_TITLE) == 'Products'

    def get_product_names(self):
        elemnets = self.find_all(self.ITEM_NAME)
        names = []
        for item in elemnets:
            names.append(item.text)
        return names

    def get_product_price(self):
        price_elements = self.find_all(self.ITEM_PRICE)

        price_as_text = []
        for el in price_elements:
            price_as_text.append(el.text)

        price_as_number = []
        for p in price_as_text:
            clean = p.replace("$", "")
            number = float(clean)
            price_as_number.append(number)

        return price_as_number

    def add_product_to_cart(self, product_name):
        itmes = self.find_all(self.INVENTORY_ITEMS)
        for item in itmes:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name.strip().lower() == product_name.strip().lower():
                item.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
                return
        raise ValueError(f"Product '{product_name}' not found")

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_product(self, option_value):
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_value(option_value)



