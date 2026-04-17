from selenium.webdriver.common.by import By
from utils.base_page import BasePage

   
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
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
        self.type(self.username_locator, username)
        

    def enter_password(self, password):
        self.type(self.password_locator, password)
        
    def click_login(self):
        self.click(self.login_btn_locator)
       
    def get_error_message(self):
        return self.get_text(self.error_message_locator)

    def get_current_url(self):
        return self.driver.current_url
    
    


