from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage



def test_checkout(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()
    
    checkout = CheckoutPage(driver)
    checkout.click_checkout()
    checkout.fill_details("ChatGpt", "OpenAI", 3180)
    checkout.finish_order()

    assert checkout.verify_success_message() == "Thank you for your order!", "Order not successed"
    
    
   
    
