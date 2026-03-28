from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.checkout_btn = (By.CSS_SELECTOR, "#checkout")
        self.continue_btn = (By.CSS_SELECTOR, "#continue")
        self.finish_btn = (By.CSS_SELECTOR, "#finish")
    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_btn)).click()

    def fill_details(self, name, lst_name, zip_code):
        first_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))
        first_name.send_keys(name)
        last_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last-name")))
        last_name.send_keys(lst_name)
        postal_code = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#postal-code")))
        postal_code.send_keys(zip_code)
        
        self.wait.until(EC.element_to_be_clickable(self.continue_btn)).click()
        
    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_btn)).click()
        

    def verify_success_message(self):
        success_message = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2"))).text

        return success_message
    
