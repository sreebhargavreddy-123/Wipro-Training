from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Generate unique email
timestamp = int(time.time())
email = f"testuser{timestamp}@gmail.com"

# Open browser
driver = webdriver.Firefox()
driver.maximize_window()

# -------------------------------------------------
# 1️⃣ Registration Form – Text boxes, Radio, Checkbox
# -------------------------------------------------
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
time.sleep(3)

# 1. Fill text boxes
driver.find_element(By.ID, "input-firstname").send_keys("Test")
driver.find_element(By.ID, "input-lastname").send_keys("User")
driver.find_element(By.ID, "input-email").send_keys(email)
driver.find_element(By.ID, "input-telephone").send_keys("9876543210")
driver.find_element(By.ID, "input-password").send_keys("Test@123")
driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

# 2. Select radio button
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

# 2. Select checkbox
driver.find_element(By.NAME, "agree").click()

# 4. Submit the form
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(3)

# 4. Verify confirmation message
confirmation = driver.find_element(
    By.XPATH, "//div[@id='content']/h1"
).text

# -------------------------------------------------
# 3️⃣ Drop-down handling using Select class
# -------------------------------------------------
driver.get("https://tutorialsninja.com/demo/index.php?route=product/category&path=20")
time.sleep(3)

dropdown = Select(driver.find_element(By.ID, "input-sort"))
dropdown.select_by_visible_text("Price (Low > High)")

print("Dropdown selected using Select class")

print("Actual confirmation text:", confirmation)

if "Your Account Has Been Created" in confirmation:
    print("Test Passed")
else:
    print("Test Failed")


# Close browser
time.sleep(3)
driver.quit()
