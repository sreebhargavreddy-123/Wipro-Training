from selenium import webdriver
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Navigate to the website
driver.get("https://example.com")

# Step 3: Print page title and URL
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

# Step 4: Wait for 3 seconds (just to see browser)
time.sleep(3)

# Step 5: Close the browser
driver.quit()
