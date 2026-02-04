import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOpenCartRegister:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)

    def teardown_method(self):
        self.driver.quit()

    def test_register(self):
        self.driver.get(
            "https://demo.opencart.com/index.php?route=account/register"
        )

        print("⏳ Complete Cloudflare verification manually")
        time.sleep(20)   # <-- YOU verify here

        self.wait.until(EC.visibility_of_element_located((By.ID, "input-firstname"))).send_keys("Sree")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Bhargav")

        email = f"sree{int(time.time())}@gmail.com"
        self.driver.find_element(By.ID, "input-email").send_keys(email)

        self.driver.find_element(By.ID, "input-password").send_keys("Bhargav@123")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        assert "Your Account Has Been Created" in self.driver.page_source
