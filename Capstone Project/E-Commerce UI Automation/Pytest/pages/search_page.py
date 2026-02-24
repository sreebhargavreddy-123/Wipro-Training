from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-box-button")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-item")
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, ".product-item h2 a")

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger)

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_BOX, product_name, "Search Box")
        self.click(self.SEARCH_BUTTON, "Search Button")

        if self.logger:
            self.logger.info(f"Searched for product: {product_name}")

    def has_results(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_ITEMS)
        )

        has_results = len(elements) > 0

        if self.logger:
            self.logger.info(f"Search results found: {has_results}")

        return has_results

    def open_first_product(self):
        self.click(self.FIRST_PRODUCT_LINK, "First Product Link")

        if self.logger:
            self.logger.info("Opened first product from search results")
