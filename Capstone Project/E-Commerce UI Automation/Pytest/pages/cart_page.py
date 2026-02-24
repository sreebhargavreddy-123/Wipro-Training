from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    QUANTITY_BOX = (By.CSS_SELECTOR, "input.qty-input")
    UPDATE_BUTTON = (By.NAME, "updatecart")
    REMOVE_CHECKBOX = (By.NAME, "removefromcart")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".order-summary-content")

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger)

    def update_quantity(self, quantity):
        self.enter_text(self.QUANTITY_BOX, quantity, "Quantity Box")
        self.click(self.UPDATE_BUTTON, "Update Cart Button")

        if self.logger:
            self.logger.info(f"Cart quantity updated to {quantity}")

    def is_quantity_updated(self, quantity):
        is_updated = str(quantity) in self.driver.page_source

        if self.logger:
            self.logger.info(f"Quantity verification result: {is_updated}")

        return is_updated

    def remove_item(self):
        self.click(self.REMOVE_CHECKBOX, "Remove Item Checkbox")
        self.click(self.UPDATE_BUTTON, "Update Cart Button")

        if self.logger:
            self.logger.info("Item removed from cart")

    def is_cart_empty(self, expected_message):
        text = self.get_text(self.EMPTY_CART_MESSAGE, "Empty Cart Message")

        is_empty = expected_message in text

        if self.logger:
            self.logger.info(f"Cart empty verification result: {is_empty}")

        return is_empty
