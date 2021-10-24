import run

# Import of driver
from selenium import webdriver

# Import of Key for Enter
from selenium.webdriver.common.keys import Keys

# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import of TimoutException
from selenium.common.exceptions import TimeoutException

# Add products to cart
def add_products(driver, product_names):
    try:
        # Check which page Im ON
        title = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='title']")))

        # Move to products Page
        if (title.text != "PRODUCTS"):
            btn = driver.find_element_by_id("react-burger-menu-btn")
            btn.click()

            inventory = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.ID, "inventory_sidebar_link")))
            inventory.click()

        # Loop Through Products
        for prod in product_names:
            try:
                # Get Button for products and click
                add_item = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        f"//div[@class='inventory_item_name'][text()='{prod}']/../../../div[@class='pricebar']/button[contains(@class, 'btn_primary')]"
                    )))
                add_item.click()
            #  Product does not exist
            except TimeoutException:
                return "Could not Find Item"
        # All Items added successfully
        return "Success"

    # Cant find title means im not logged in
    except TimeoutException:
        return "User at login page"


# Check if list products are in cart
def are_products_in_cart(driver, product_names):
    try:
        # Check which page Im ON
        title = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='title']")))

        # Move to shopping cart Page
        if (title.text != "YOUR CART"):
            btn = driver.find_element_by_xpath(
                "//div[@id='shopping_cart_container']/a")
            btn.click()

        # Loop Through Products
        for prod in product_names:
            try:
                # Look for items
                add_item = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        f"//div[@class='inventory_item_name'][text()='{prod}']"
                    )))

            # No item in cart matches name
            except TimeoutException:
                return "Could not Find Item"

        # All Items Found
        return "Success"

    # Cant find title means im not logged in
    except TimeoutException:
        return "User at login page"

## Run with specific inputs
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://saucedemo.com")

    username = "standard_user"
    password = "secret_sauce"

    print(run.login(driver, username, password))

    list_of_products = [
        "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"
    ]
    print(add_products(driver, list_of_products))
    print(are_products_in_cart(driver, list_of_products))

    driver.quit()
