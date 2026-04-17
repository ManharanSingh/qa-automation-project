from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME, PASSWORD
from utils.logger import get_logger


logger = get_logger(__name__)

def test_cart(driver_setup ):
    driver = driver_setup
    login_page = LoginPage(driver)
    
    logger.info("Opening login page")
    login_page.open(BASE_URL)
    logger.info("Entering username and password")
    login_page.login(USERNAME, PASSWORD)
    
    inventory = InventoryPage(driver)
    
    logger.info("Adding item to cart") 
    inventory.add_to_cart()
    
    logger.info("Navigating to cart page")
    inventory.go_to_cart()
    
    cart_count = inventory.get_cart_count()
    logger.info(f"Cart count after adding item: {cart_count}")
    
    assert inventory.get_cart_count() == 1, f"Expected cart count 1, but got {cart_count}"
    
    inventory.remove_item()
    
    updated_count = inventory.get_removed_items_count()
    logger.info(f"Cart count after removing item: {updated_count}")
    
    logger.info("verifying empty cart")
    assert inventory.get_removed_items_count() == 0, f"Expected empty cart, but got {updated_count}"
    


    
