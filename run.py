# Import of driver
from selenium import webdriver

import src.login_page as login_page

## Run with specific inputs
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://saucedemo.com")

    username = "standard_user"
    password = "secret_sauce"

    ProductsPage = login_page.LoginPage(driver).login(username, password)

    list_of_products = [
        "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"
    ]
    ProductsPage.add_products(list_of_products)
    CartPage = ProductsPage.goto_Cart_page()
    print(CartPage.are_products_in_cart(list_of_products))


    driver.quit()
