from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Setup Edge WebDriver
service = Service()
driver = webdriver.Edge(service=service)

driver.maximize_window()
driver.implicitly_wait(5)

# Open the website
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# 1️⃣ Trigger JavaScript Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

alert = driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()   # Accept alert

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result:", result)
assert "You successfully clicked an alert" in result


# 2️⃣ Trigger Confirmation Pop-up and Dismiss
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

confirm_alert = driver.switch_to.alert
print("Confirm Message:", confirm_alert.text)
confirm_alert.dismiss()   # Dismiss alert

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result:", result)
assert "You clicked: Cancel" in result


# 3️⃣ Trigger Prompt Alert and Enter Text
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

prompt_alert = driver.switch_to.alert
print("Prompt Message:", prompt_alert.text)

prompt_alert.send_keys("Selenium Automation")
prompt_alert.accept()

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result:", result)
assert "Selenium Automation" in result


# Close browser
time.sleep(2)
driver.quit()
