import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTest1():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1(self):
        self.driver.get("https://www.google.com/")
        self.driver.set_window_size(1050, 652)

        # Wait for search box and type
        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("software testing")
