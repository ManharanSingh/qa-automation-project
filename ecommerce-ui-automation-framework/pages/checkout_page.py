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

    def fill_details(self, name, last_name, zip_code):
            
            name_element = self.wait.until(EC.visibility_of_element_located(self.first_name_locator))
            name_element.send_keys(name)
            if not lambda d: self.driver.find_element(*self.first_name_locator).get_attribute("value") != name):
                   self.type(self.first_name_locator, name)
                    
            self.driver.save_screenshot("name_filled.png")
            
            last_name_element = self.wait.until(EC.visibility_of_element_located(self.last_name_locator))
            last_name_element.send_keys(last_name)
            
            zip_code_element = self.wait.until(EC.visibility_of_element_located(self.postal_code_locator))
            zip_code_element.send_keys(zip_code)
            if not lambda d: self.driver.find_element(*self.postal_code_locator).get_attribute("value") != zip_code):
                   self.type(self.postal_code_locator, name)
                    
            self.driver.save_screenshot("zip_code_filled.png")   
            
            self.click(self.continue_btn)
            self.driver.save_screenshot("test.png")
       
       
    
    def finish_order(self):
        self.click(self.finish_btn)
        
    def verify_success_message(self):
        success_message = self.get_text(self.success_message)

        return success_message
    
