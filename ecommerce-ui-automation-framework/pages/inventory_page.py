from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.backpack_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.remove_backpack_btn = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
        
        
    def add_to_cart(self):
       self.click(self.backpack_btn)

    def go_to_cart(self):
        self.click(self.cart_button)

    def get_cart_count(self):
        cart_list =self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
        
        return len(cart_list)  
    
    def remove_item(self):
        self.click(self.remove_backpack_btn)

    def get_removed_items_count(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        
        return len(items)
        
     
