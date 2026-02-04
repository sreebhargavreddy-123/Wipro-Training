from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_locators_object_identification():
    # Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open TutorialsNinja Demo site
    driver.get("https://tutorialsninja.com/demo/")

    # ---------- USING LINK TEXT (extra) ----------
    driver.find_element(By.LINK_TEXT, "My Account").click()
    driver.find_element(By.LINK_TEXT, "Login").click()

    wait = WebDriverWait(driver, 10)

    # ---------- ID LOCATOR ----------
    email = wait.until(EC.presence_of_element_located((By.ID, "input-email")))
    email.send_keys("invalid@test.com")

    # ---------- NAME LOCATOR ----------
    password = driver.find_element(By.NAME, "password")
    password.send_keys("wrongpassword")

    # ---------- CSS SELECTOR ----------
    login_btn = driver.find_element(By.CSS_SELECTOR, "input[value='Login']")
    login_btn.click()

    # ---------- CLASS NAME LOCATOR ----------
    warning_msg = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # ---------- XPATH LOCATOR (extra validation) ----------
    warning_xpath = driver.find_element(
        By.XPATH, "//div[contains(@class,'alert-danger')]"
    )

    # ---------- VALIDATION ----------
    assert "No match for E-Mail Address" in warning_msg.text
    assert warning_msg.text == warning_xpath.text

    # Close browser
    driver.quit()
