import pytest
from selenium import webdriver

import src.login_page as login_page

# Open a new instance for each test
@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.get("https://saucedemo.com")
    return driver

# Test a bad username/password
def test_bad_userpass(driver):
    ProductsPage = login_page.LoginPage(driver).login("asdf","asdf")
    assert ProductsPage == "Epic sadface: Username and password do not match any user in this service"
    driver.quit()

# Test a standard user
def test_standard_user(driver):
    ProductsPage = login_page.LoginPage(driver).login("standard_user", "secret_sauce")
    assert ProductsPage.is_Products_Page()
    driver.quit()

# Test a locked user
def test_locked_out_user(driver):
    ProductsPage = login_page.LoginPage(driver).login("locked_out_user", "secret_sauce")
    assert ProductsPage == "Epic sadface: Sorry, this user has been locked out."
    driver.quit()

# Test a user with a problematic products page
def test_problem_user(driver):
    ProductsPage = login_page.LoginPage(driver).login("problem_user", "secret_sauce")
    assert ProductsPage.is_Products_Page()
    driver.quit()

# Test a user with a poor performing network
def test_performance_glitch_user(driver):
    ProductsPage = login_page.LoginPage(driver).login("performance_glitch_user", "secret_sauce")
    assert ProductsPage.is_Products_Page()
    driver.quit()
