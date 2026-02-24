from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My account")

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger)

    def login(self, email, password):
        self.enter_text(self.EMAIL, email, "Email Field")
        self.enter_text(self.PASSWORD, password, "Password Field")
        self.click(self.LOGIN_BUTTON, "Login Button")

    def is_login_successful(self):
        is_displayed = self.wait.until(
            lambda driver: driver.find_element(*self.MY_ACCOUNT_LINK).is_displayed()
        )

        if self.logger:
            self.logger.info("Login successful - My Account link is visible")

        return is_displayed
