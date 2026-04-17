from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME, PASSWORD
from utils.logger import get_logger
from config.config import FIRST_NAME, LAST_NAME, ZIP_CODE
import time

logger = get_logger(__name__)

def test_checkout(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    logger.info("Opening login page")
    login_page.open(BASE_URL)
    logger.info("Entering username and password")
    login_page.login(USERNAME, PASSWORD)
    
    inventory = InventoryPage(driver)
    time.sleep(3)
    logger.info("Adding item to cart")
    inventory.add_to_cart()
    time.sleep(3)
    logger.info("Navigating to cart page")
    inventory.go_to_cart()
    time.sleep(3)
    checkout = CheckoutPage(driver)

    logger.info("Navigating to checkout page")
    checkout.click_checkout()
    time.sleep(3)
    logger.info("Entering checkout details: first_name=Manharan, last_name=Maravi, zip=501401")
    checkout.fill_details(FIRST_NAME, LAST_NAME, ZIP_CODE)
    time.sleep(3)
    logger.info("Finishing checkout process")
    checkout.finish_order()
    time.sleep(3)
    success_msg = checkout.verify_success_message()
    logger.info(f"Order success message: {success_msg}")
    time.sleep(3)
    assert success_msg == "Thank you for your order!", \
    f"Expected success message not found. Got: {success_msg}"
   
    
