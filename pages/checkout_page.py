from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error'")
    TOTAL_AMOUNT_LABEL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ZIP_CODE_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_total_amount(self):
        return self.get_text(self.TOTAL_AMOUNT_LABEL)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_completion_message(self):
        return self.get_text(self.COMPLETE_HEADER)
