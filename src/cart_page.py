# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import of TimoutException
from selenium.common.exceptions import TimeoutException

class CartPage:
    def __init__(self, driver):
        self.driver = driver

        self.title = (By.XPATH, "//span[@class='title']")

    def create_cart_XPATH(self, prod):
        return (
            By.XPATH,
            f"//div[@class='inventory_item_name'][text()='{prod}']"
        )


    # Check if list products are in cart
    def are_products_in_cart(self, product_names):
        if(self.is_Cart_Page() is False):
            return "Wrong Page"

        # Loop Through Products
        for prod in product_names:
            try:
                # Look for items
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(self.create_cart_XPATH(prod)))
            # No item in cart matches name
            except TimeoutException:
                print(f"Could not Find Item: {prod}")
        # All Items Found
        return "Success"

    def is_Cart_Page(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.title)).text == "YOUR CART"
        except TimeoutException:
            return False
