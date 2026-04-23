from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

   
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        
        
    def type(self, locator, text):
       element = self.wait.until(EC.visibility_of_element_located(locator))
       self.wait.until(lambda d: element.is_enabled())
       element.clear()
       element.send_keys(text)
       verify = element.get_attribute("value")
       time.sleep(1)
       sec_verify = element.get_attribute("value")
       
       if verify != sec_verify:
          raise ValueError("Js is clearing it ")
           
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
   
