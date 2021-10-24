from selenium import webdriver
import pytest
import run
import cart


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
    res = cart.add_products(driver, list_of_products)
    driver.quit()
    assert res == "User at login page"


# Test a standard user
def test_add_logged_in(driver):
    run.login(driver, "standard_user", "secret_sauce")

    list_of_products = [
        "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"
    ]
    res = cart.add_products(driver, list_of_products)
    driver.quit()
    assert res == "Success"


# Test a standard user
def test_cart_logged_in(driver):
    run.login(driver, "standard_user", "secret_sauce")

    list_of_products = [
        "Sauce Labs Backpack", "Test.allTheThings() T-Shirt (Red)"
    ]
    cart.add_products(driver, list_of_products)
    res = cart.are_products_in_cart(driver, list_of_products)
    driver.quit()
    assert res == "Success"
