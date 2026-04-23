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
        print("Before:", element.get_attribute("value"))
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        
        print("After:", element.get_attribute("value"))
        time.sleep(2)
        print("After 2 sec:", element.get_attribute("value"))
        
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
   
