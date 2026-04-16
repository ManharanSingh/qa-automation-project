import pytest
from pages.login_page import LoginPage
from config.config import BASE_URL
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("username, password, expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False)
])
 
def test_login(driver_setup, username, password, expected):
        driver = driver_setup
        login_page = LoginPage(driver)
        
        logger.info("opening login page")  
        login_page.open(BASE_URL)
        logger.info("Entering username and password")
        login_page.login(username, password) 
        
        
        if expected:
            logger.info("Login successful, verifying URL")
            assert "inventory" in login_page.get_current_url()

        else:
            error = login_page.get_error_message().lower()
            logger.info(f"login failed with error :{error}")
            assert "locked out" in error  
                
        
            
       


