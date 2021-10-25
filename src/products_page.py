# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import of TimoutException
from selenium.common.exceptions import TimeoutException

# Import Other Pages
import src.cart_page as cart_page


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

        self.title = (By.XPATH, "//span[@class='title']")

    def create_product_XPATH(self, prod):
        return (
            By.XPATH,
            f"//div[@class='inventory_item_name'][text()='{prod}']/../../../div[@class='pricebar']/button[contains(@class, 'btn_primary')]"
        )

    # Add products to cart
    def add_products(self, product_names):
        if (self.is_Products_Page() is False):
            return "Wrong Page"

        # Loop Through Products
        for prod in product_names:
            try:
                # Get Button for products and click
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.create_product_XPATH(prod))).click()
            #  Product does not exist
            except TimeoutException:
                print(f"Could not Find Item: {prod}")
        # All Items added successfully
        return "Success"

    def is_Products_Page(self):
        try:
            return WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.title)).text == "PRODUCTS"
        except TimeoutException:
            return False

    def goto_Cart_page(self):
        self.driver.find_element_by_xpath("//div[@id='shopping_cart_container']/a").click()
        return cart_page.CartPage(self.driver)
