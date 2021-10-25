# Import of Key for Enter
from selenium.webdriver.common.keys import Keys

# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import of TimoutException
from selenium.common.exceptions import TimeoutException

# Import Other Pages
import src.products_page as products_page


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.err = (By.XPATH, "//div[@class='error-message-container error']/h3")
        self.title = (By.XPATH, "//span[@class='title']")

    # The login function
    def login(self, username, password):
        # The username input and keystrokes
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)

        # The password input and keystrokes and submit of form
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password, Keys.ENTER)

        # Looking for error. 3 seconds to account for latency
        try:
            # If Error, return error text
            return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.err)).text

        # Error Times out, ie. No Error.
        # Ensuring proper login to products page.
        # 15 seconds to account for user latency
        except TimeoutException:
            print("Test")
            return products_page.ProductsPage(self.driver)

    # Checks if current Page is Login Page
    def is_Login_Page(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.title))
            return False
        except TimeoutException:
            return True
