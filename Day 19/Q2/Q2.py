from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

GRID_URL = "http://localhost:4444"

browsers = [
    ("chrome", ChromeOptions()),
    ("firefox", FirefoxOptions())
]

for browser_name, options in browsers:
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    try:
        driver.get("https://www.google.com")

        # Verify title
        assert "Google" in driver.title

        # Print browser & platform
        caps = driver.capabilities
        print("Browser Name :", caps.get("browserName"))
        print("Platform     :", caps.get("platformName"))
        print("Title Check  : PASSED")
        print("-" * 40)

    except AssertionError:
        print("Title verification FAILED")

    finally:
        time.sleep(2)
        driver.quit()
