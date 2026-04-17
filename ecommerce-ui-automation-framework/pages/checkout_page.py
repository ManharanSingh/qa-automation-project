from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_locator = (By.CSS_SELECTOR, "#first-name")
        self.last_name_locator = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_locator = (By.CSS_SELECTOR, "#postal-code")
        self.checkout_btn = (By.ID, "checkout")
        self.continue_btn = (By.CSS_SELECTOR, "#continue")
        self.finish_btn = (By.ID, "#finish")
        self.success_message = (By.TAG_NAME, "h2")

    def click_checkout(self):
        self.click(self.checkout_btn)

    def fill_details(self, name, last_name, zip_code):
        self.type(self.first_name_locator, name)
        self.type(self.last_name_locator, last_name)
        self.type(self.postal_code_locator, zip_code)
        self.click(self.continue_btn)
        
    def finish_order(self):
        self.click(self.finish_btn)
        
    def verify_success_message(self):
        success_message = self.get_text(self.success_message)

        return success_message
    
