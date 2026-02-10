from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# ============================
# CONFIGURATION
# ============================
class Config:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"

# ============================
# BASE PAGE (Reusable Actions)
# ============================
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

# ============================
# PAGE OBJECT: Login Page
# ============================
class LoginPage(BasePage):
    # Locators
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    # Actions
    def login(self, username, password):
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click(self.login_button)

    def get_error_text(self):
        return self.get_text(self.error_message)

# ============================
# BROWSER SETUP (PyTest fixture)
# ============================
@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(5)

    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

# ============================
# TEST CASES
# ============================
def test_login_invalid(setup):
    """
    Scenario: Invalid login should display an error message
    """
    login_page = LoginPage(setup)

    # Attempt wrong credentials
    login_page.login("wronguser", "wrongpass")
    error_text = login_page.get_error_text()

    print("Invalid login message:", error_text)
    assert "Invalid credentials" in error_text

def test_login_valid(setup):
    """
    Scenario: Valid login should succeed
    """
    login_page = LoginPage(setup)

    login_page.login(Config.USERNAME, Config.PASSWORD)

    # After successful login, URL of dashboard typically contains '/dashboard'
    assert "/dashboard" in setup.current_url
    print("Dashboard URL after login:", setup.current_url)
