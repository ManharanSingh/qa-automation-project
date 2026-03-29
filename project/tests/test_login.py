import pytest
import logging
from pages.login_page import LoginPage


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s -%(levelname)s -%(message)s")

@pytest.mark.parametrize("username, password, expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False)
])
 
 
def test_login(driver_setup, username, password, expected):
        driver = driver_setup
        login_page = LoginPage(driver)
        
        logging.info("opening login page")
        login_page.open("https://www.saucedemo.com/")
        logging.info("Entering username and password")
        login_page.login(username, password) 
        
        try:
            if expected:
                logging.info("Login successful, verifying URL")
                assert "inventory" in login_page.get_current_url()

            else:
                error = login_page.get_error_message().lower()
                logging.info(f"login failed with error :{error}")
                assert "locked out" in error  
                
        except AssertionError:
            logging.error("Test failed, capturing screenshot")
            driver.save_screenshot(f'{username}_fail.png')   
            raise      
        
            
       


