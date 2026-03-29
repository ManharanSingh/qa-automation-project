from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 

   
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_locator = (By.CSS_SELECTOR, "#user-name")
        self.password_locator = (By.CSS_SELECTOR, "#password")
        self.login_btn_locator = (By.CSS_SELECTOR, "#login-button")
        self.error_message_locator = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self, link):
        self.driver.get(link)
     
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
     
    def enter_username(self, username):
        username_section = self.wait.until(EC.visibility_of_element_located(self.username_locator))
        username_section.send_keys(username)
        

    def enter_password(self, password):
        password_section = self.wait.until(EC.visibility_of_element_located(self.password_locator))
        password_section.send_keys(password)
        

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn_locator)).click()
       
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message_locator)).text
        
    def get_current_url(self):
        return self.driver.current_url
    
    def get_driver(self):
        return self.driver

