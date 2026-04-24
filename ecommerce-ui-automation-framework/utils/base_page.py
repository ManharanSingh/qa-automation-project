from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
        
    def login_type(self, locator, text):
       element =  self.wait.until(EC.visibility_of_element_located(locator))
       element.clear()
       element.send_keys(text)
       
    def type(self, locator, text):
       element = self.wait.until(EC.element_to_be_clickable(locator))
       elements = self.driver.find_elements(*locator)
       logger.info(f"element count:{len(elements)}")     
       element.click()
       self.driver.execute_script("arguments[0].focus();", element)    
       self.driver.execute_script("""arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input', { bubbles: true }));arguments[0].dispatchEvent(new Event('change', { bubbles: true }));""", element, text) 
       self.driver.execute_script("arguments[0].blur();", element)   
       self.wait.until(lambda d: element.get_attribute("value") != "")      
       active = self.driver.switch_to.active_element
       if active != element:
          raise ValueError("focus issue")
       logger.info(f"before : {element}")
       logger.info(f"Tag:{element.tag_name}")
       logger.info(f"Type:{element.get_attribute('type')}")
       logger.info(f"verify 1: {element.is_displayed()}")
       logger.info(f"verify 2: {element.is_enabled()}")

       rect = element.rect
       logger.info(f"verify 3:{rect}")                 
       self.driver.execute_script("arguments[0].value = arguments[1];", element, text)
       element = self.driver.find_element(*locator)
       logger.info(f"new element:{element.get_attribute('value')}")
         
          
       logger.info(f"immediate : {element.get_attribute('value')}")
       time.sleep(0.5)
       logger.info(f"After 0.5s:{element.get_attribute('value')}")
       new_element = self.driver.find_element(*locator)
       logger.info(f"after : {new_element}")
       logger.info(f"same element? :{element == new_element}")
       value_after = element.get_attribute("value")
       if value_after != text:
          raise ValueError(f"value after typing:{value_after}")

       
       time.sleep(1)

       value_later = element.get_attribute("value")
       if value_later != text:
          raise ValueError("value after 1s:", value_later)
       
       return element
       
       
       
       
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
   
