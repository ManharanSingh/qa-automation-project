from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.logger import get_logger

logger = get_logger(__name__)
   
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
       element = self.wait.until(EC.element_to_be_clickable(locator))
       element.click()
       self.driver.execute_script("arguments[0].focus();", element)
       active = self.driver.switch_to.active_element
       if active != element:
          raise ValueError("focus issue")
       logger.info(f"before : {element}")
       element.send_keys(text)
       logger.info(f"immediate : {element.get_attribute('value')}")
       import time
       time.sleep(0.5)
       logger.info(f"After 0.5s:{element.get_attribute('value')}")
       new_element = self.driver.find_element(*locator)
       logger.info(f"after : {new_element}")
       logger.info(f"same element? :{element == new_element}")
       value_after = element.get_attribute("value")
       if value_after != text:
          raise ValueError(f"value after typing:{value_after}")

       import time
       time.sleep(1)

       value_later = element.get_attribute("value")
       if value_later != text:
          raise ValueError("value after 1s:", value_later)
       
       
       
       
       
       
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
   
