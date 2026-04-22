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
        element.click()
        self.wait.until(lambda d, el=element: d.execute_script("return document.activeElement === arguments[0];", el))
        element.clear()
        element.send_keys(text)

        actual = element.get_attribute("value")
        assert actual == text , f"{locator} mismatch! got :{actual}"
                        
        
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
   
