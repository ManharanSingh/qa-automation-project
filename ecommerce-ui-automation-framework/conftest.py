import pytest
from selenium import webdriver


@pytest.fixture
def driver_setup():
   
    driver = webdriver.Edge()    
    yield driver

    driver.quit()  

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver_setup")

        if driver:
            screenshot_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)
