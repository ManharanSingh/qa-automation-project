import pytest
from selenium import webdriver
import os

@pytest.fixture
def driver_setup():
   from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver_setup():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver_setup")

        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)
