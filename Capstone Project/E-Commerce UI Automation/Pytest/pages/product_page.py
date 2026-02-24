from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product-name h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product-price span")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input.button-1.add-to-cart-button")
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, "div.bar-notification.success")

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger)

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE, "Product Title")

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE, "Product Price").strip()

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON, "Add To Cart Button")

    def get_success_notification(self):
        return self.get_text(self.SUCCESS_NOTIFICATION, "Success Notification")
