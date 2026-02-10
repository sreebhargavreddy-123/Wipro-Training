from selenium import webdriver
from loginpage import LoginPage

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

loginobj = LoginPage(driver)
loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()
