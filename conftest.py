import pytest
from selenium import webdriver


@pytest.fixture
def driver_setup():
   
    driver = webdriver.Edge()    
    yield driver

    driver.quit()  