from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


   
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
   
        for attempt in range(3):
           element = self.wait.until(EC.element_to_be_clickable(locator))
           self.wait.until(lambda d: element.is_enabled())
           element.clear()
           element.send_keys(text)
           
    
           if element.get_attribute("value") == text:
              break
           else:
              raise Exception("Input not stable after retries")
              
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
   
