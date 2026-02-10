from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# --------------------------------------------------
# 1️⃣ Implicit Wait
# --------------------------------------------------
# Selenium will wait up to 10 seconds for elements to appear
driver.implicitly_wait(10)
print("Implicit wait applied (10 seconds)")

# Click on Google Search box (example element)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium waits")
print("Element found using implicit wait")

# --------------------------------------------------
# 2️⃣ Explicit Wait – Wait until element is clickable
# --------------------------------------------------
wait = WebDriverWait(driver, 10)

search_button = wait.until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)

print("Explicit wait: Element is clickable now")
search_button.click()

# --------------------------------------------------
# 3️⃣ Fluent Wait – with polling interval
# --------------------------------------------------
fluent_wait = WebDriverWait(
    driver,
    timeout=15,
    poll_frequency=2,                 # polling every 2 seconds
    ignored_exceptions=[NoSuchElementException]
)

search_box_fluent = fluent_wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# --------------------------------------------------
# 4️⃣ Print message when element is available
# --------------------------------------------------
print("Fluent wait: Element is available for interaction")

time.sleep(3)
driver.quit()
