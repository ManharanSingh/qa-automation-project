from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



             

         
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
       element.click()
       self.driver.execute_script("arguments[0].focus();", element)    
       self.driver.execute_script(""" 
       const input = arguments[0]; 
       const val = arguments[1]; 
       const lastValue = input.value; 
       input.value = val; 
       const event = new Event('input',{bubbles:true});
       const tracker = input._valueTracker;

       if (tracker){
          tracker.setValue(lastValue);
          }
       input.dispatchEvent(event);
       """, element, text)
       
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
   
