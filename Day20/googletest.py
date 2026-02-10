import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driverfactory import get_driver


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_googletitle(browser):
    driver = get_driver(browser)
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.google.com")

    # Wait until search box appears
    wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Assert Google page loaded
    assert "Google" in driver.page_source

    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_search(browser):
    driver = get_driver(browser)
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.google.com")

    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("selenium grid")
    search_box.submit()

    # Wait until results page loads
    wait.until(EC.title_contains("selenium"))

    assert "selenium" in driver.title.lower()

    driver.quit()
