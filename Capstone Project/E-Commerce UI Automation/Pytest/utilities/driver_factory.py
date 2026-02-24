from selenium import webdriver
from utilities.config_reader import ConfigReader

class DriverFactory:

    @staticmethod
    def get_driver():
        browser = ConfigReader.get_browser().lower()

        # =====================
        # Chrome Browser
        # =====================
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)

        # =====================
        # Firefox Browser
        # =====================
        elif browser == "firefox":
            driver = webdriver.Firefox()
            driver.maximize_window()

        # =====================
        # Edge Browser
        # =====================
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(options=options)

        # =====================
        # Unsupported Browser
        # =====================
        else:
            raise Exception(f"Browser not supported: {browser}")

        # Global implicit wait
        driver.implicitly_wait(ConfigReader.get_implicit_wait())
        return driver
