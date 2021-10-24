from selenium import webdriver
import pytest
import run

# Open a new instance for each test
@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.get("https://saucedemo.com")
    return driver

# Test a bad username/password
def test_bad_userpass(driver):
    res = run.login(driver, "asdf","asdf")
    driver.quit()
    assert res == "Epic sadface: Username and password do not match any user in this service"

# Test a standard user
def test_standard_user(driver):
    res = run.login(driver, "standard_user", "secret_sauce")
    driver.quit()
    assert res == "PRODUCTS"

# Test a locked user
def test_locked_out_user(driver):
    res = run.login(driver, "locked_out_user", "secret_sauce")
    driver.quit()
    assert res == "Epic sadface: Sorry, this user has been locked out."

# Test a user with a problematic products page
def test_problem_user(driver):
    res = run.login(driver, "problem_user", "secret_sauce")
    driver.quit()
    assert res == "PRODUCTS"

# Test a user with a poor performing network
def test_performance_glitch_user(driver):
    res = run.login(driver, "performance_glitch_user", "secret_sauce")
    driver.quit()
    assert res == "PRODUCTS"
