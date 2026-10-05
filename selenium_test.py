from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.saucedemo.com/")

# Login
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login.click()

# Find products
products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

# Print first 5 products
for i in range(5):
    print(products[i].text)

input("Press Enter to close...")
driver.quit()