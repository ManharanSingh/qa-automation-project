from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time
        
class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_locator = (By.ID, "first-name")
        self.last_name_locator = (By.ID, "last-name")
        self.postal_code_locator = (By.ID, "postal-code")
        self.checkout_btn = (By.ID, "checkout")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.success_message = (By.TAG_NAME, "h2")

    def click_checkout(self):
        self.click(self.checkout_btn)

        self.wait.until(EC.url_contains("checkout-step-one"))
        
    def fill_details(self, name, last_name, zip_code):
             
              NAME = self.driver.find_element(self.first_name_locator)
              NAME.send_keys(name)
              
              Last_Name = self.driver.find_element(self.last_name_locator)
              Last_Name.send_keys(last_name)
              
              Zip_Code = self.driver.find_element(self.postal_code_locator)
              Zip_Code.send_keys(zip_code)
             
              
              self.click(self.continue_btn)
       
       
    
    def finish_order(self):
        self.click(self.finish_btn)
        
    def verify_success_message(self):
        success_message = self.get_text(self.success_message)

        return success_message
    
