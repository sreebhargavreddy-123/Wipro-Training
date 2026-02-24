from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    REGISTER_LINK = (By.LINK_TEXT, "Register")
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")
    CART_LINK = (By.LINK_TEXT, "Shopping cart")

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger)

    def click_register(self):
        self.click(self.REGISTER_LINK, "Register Link")

    def click_login(self):
        self.click(self.LOGIN_LINK, "Login Link")

    def click_logout(self):
        self.click(self.LOGOUT_LINK, "Logout Link")

    def click_cart(self):
        self.click(self.CART_LINK, "Shopping Cart Link")
