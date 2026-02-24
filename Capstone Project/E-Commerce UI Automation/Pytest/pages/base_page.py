from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from utilities.config_reader import ConfigReader


class BasePage:

    def __init__(self, driver, logger=None):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, ConfigReader.get_explicit_wait())

    def click(self, locator, element_name="Element"):
        for _ in range(3):
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()

                if self.logger:
                    self.logger.info(f"Clicked on {element_name}")

                return
            except StaleElementReferenceException:
                if self.logger:
                    self.logger.warning(
                        f"Retrying click on {element_name} due to stale element"
                    )
                continue

    def enter_text(self, locator, text, element_name="Element"):
        for _ in range(3):
            try:
                element = self.wait.until(
                    EC.visibility_of_element_located(locator)
                )
                element.clear()
                element.send_keys(text)

                if self.logger:
                    self.logger.info(f"Entered '{text}' into {element_name}")

                return
            except StaleElementReferenceException:
                if self.logger:
                    self.logger.warning(
                        f"Retrying enter_text on {element_name} due to stale element"
                    )
                continue

    def get_text(self, locator, element_name="Element"):
        for _ in range(3):
            try:
                text = self.wait.until(
                    EC.visibility_of_element_located(locator)
                ).text

                if self.logger:
                    self.logger.info(
                        f"Retrieved text from {element_name}: {text}"
                    )

                return text
            except StaleElementReferenceException:
                if self.logger:
                    self.logger.warning(
                        f"Retrying get_text on {element_name} due to stale element"
                    )
                continue
