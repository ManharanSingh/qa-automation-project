from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_cart(driver_setup ):
    driver = driver_setup
    login_page = LoginPage(driver)
    

    login_page.open("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    
    inventory = InventoryPage(driver)

    inventory.add_to_cart()
    inventory.go_to_cart()
    assert inventory.get_cart_count() == 1, "cart count test failed"
    inventory.remove_item()
    assert inventory.get_removed_items_count() == 0, "empty cart verification  failed"
    


    
