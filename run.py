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

# The login function
def login(driver, username,password):
    # The username input and keystrokes
    user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID,
            "user-name")))
    user.send_keys(username)

    # The password input and keystrokes and submit of form
    passw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    passw.send_keys(password, Keys.ENTER)

    # Looking for error. 3 seconds to account for latency
    try:
        err = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//div[@class='error-message-container error']/h3")))
        # If Error, return error text
        return err.text
    # Error Times out, ie. No Error.
    # Ensuring proper login to products page.
    # 15 seconds to account for user latency
    except TimeoutException:
        # The product Header
        product = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH,
                    "//span[@class='title']")))
        return product.text




## Run with specific inputs
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://saucedemo.com")

    username = "standard_user"
    password = "secret_sauce"

    print(login(driver, username, password))
