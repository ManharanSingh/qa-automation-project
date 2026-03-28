from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.backpack_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.remove_backpack_btn = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
        
        
    def add_to_cart(self):
       self.wait.until(EC.element_to_be_clickable(self.backpack_btn)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()

    def get_cart_count(self):
        cart_list =self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
        
        return len(cart_list)  
    
    def remove_item(self):
        self.wait.until(EC.element_to_be_clickable(self.remove_backpack_btn)).click()

    def get_removed_items_count(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        
        return len(items)
        
     
