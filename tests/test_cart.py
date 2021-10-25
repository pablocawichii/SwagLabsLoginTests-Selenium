from selenium import webdriver
import pytest

import src.login_page as login_page
import src.products_page as products_page


# Open a new instance for each test
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://saucedemo.com")
    return driver

# Test a standard user
def test_add_not_logged_in(driver):
    list_of_products = [
        "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"
    ]
    assert products_page.ProductsPage(driver).add_products(list_of_products) == "Wrong Page"
    driver.quit()


# Test a standard user
def test_add_logged_in(driver):
    list_of_products = [
        "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"
    ]

    ProductsPage = login_page.LoginPage(driver).login("standard_user", "secret_sauce")
    assert ProductsPage.add_products(list_of_products) == "Success"
    driver.quit()


# Test a standard user
def test_cart_logged_in(driver):
    list_of_products = [
        "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"
    ]

    ProductsPage = login_page.LoginPage(driver).login("standard_user", "secret_sauce")
    ProductsPage.add_products(list_of_products)
    CartPage = ProductsPage.goto_Cart_page()
    assert CartPage.are_products_in_cart(list_of_products) == "Success"
    driver.quit()
