from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# ---------------- Browser Setup ----------------
service = Service()
driver = webdriver.Edge(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# =================================================
# 1. Switch to iframe and enter text inside it
# =================================================
driver.get("https://the-internet.herokuapp.com/iframe")

# Switch to iframe
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

# Enter text inside iframe (TinyMCE editor)
editor = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
actions = ActionChains(driver)
actions.click(editor)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
actions.send_keys(Keys.DELETE)
actions.send_keys("Sree Bhargav Reddy")
actions.perform()

print("Entered text inside iframe")

# =================================================
# 2. Switch back to main content
# =================================================
driver.switch_to.default_content()
print("Switched back to main content")

# =================================================
# 3. Open a new browser window (OrangeHRM)
# =================================================
parent_window = driver.current_window_handle
driver.execute_script(
    "window.open('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login','_blank');"
)
time.sleep(3)

# =================================================
# 4. Switch between windows and print each title
# =================================================
all_windows = driver.window_handles
for window in all_windows:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)

# =================================================
# 5. Close child window and return to parent
# =================================================
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()
        print("Child window closed")

driver.switch_to.window(parent_window)
print("Returned to parent window")

time.sleep(3)
driver.quit()
