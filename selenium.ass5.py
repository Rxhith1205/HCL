from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://demo.automationtesting.in/Register.html")

print("==============================================")
print("AUTOMATION TESTING REGISTRATION - XPATH")
print("==============================================")


# TC01 - Open page
try:
    driver.get("https://demo.automationtesting.in/Register.html")
    print("TC01 - PASS - Page opened")
except:
    print("TC01 - FAIL")


# TC02 - Attribute XPath
try:
    driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Rohith")
    print("TC02 - PASS - Username located")
except:
    print("TC02 - FAIL")


# TC03 - Password
try:
    driver.find_element(By.XPATH, "//input[@id='firstpassword']").send_keys("Selenium@123")
    print("TC03 - PASS - Password entered")
except:
    print("TC03 - FAIL")


# TC04 - text()
try:
    submit = driver.find_element(By.XPATH, "//button[text()='Submit']")
    print("TC04 - PASS - Submit located:", submit.text)
except:
    print("TC04 - FAIL")


# TC05 - contains()
try:
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Name')]")
    print("TC05 - PASS - contains()")
except:
    print("TC05 - FAIL")


# TC06 - starts-with()
try:
    driver.find_element(By.XPATH, "//input[starts-with(@placeholder,'Last')]")
    print("TC06 - PASS - starts-with()")
except:
    print("TC06 - FAIL")


# TC07 - and
try:
    driver.find_element(By.XPATH, "//input[@placeholder='First Name' and @type='text']")
    print("TC07 - PASS - and")
except:
    print("TC07 - FAIL")


# TC08 - or
try:
    names = driver.find_elements(By.XPATH, "//input[@placeholder='First Name' or @placeholder='Last Name']")
    print("TC08 - PASS - or | Fields:", len(names))
except:
    print("TC08 - FAIL")


# TC09 - parent
try:
    parent = driver.find_element(By.XPATH, "//input[@placeholder='First Name']/parent::*")
    print("TC09 - PASS - Parent:", parent.tag_name)
except:
    print("TC09 - FAIL")


# TC10 - ancestor
try:
    form = driver.find_element(By.XPATH, "//input[@placeholder='First Name']/ancestor::form")
    print("TC10 - PASS - Form:", form.get_attribute("id"))
except:
    print("TC10 - FAIL")


# TC11 - child
try:
    children = driver.find_elements(By.XPATH, "//form/child::*")
    print("TC11 - PASS - Children:", len(children))
except:
    print("TC11 - FAIL")


# TC12 - following
try:
    following = driver.find_elements(By.XPATH, "//input[@placeholder='First Name']/following::*")
    print("TC12 - PASS - Following:", len(following))
except:
    print("TC12 - FAIL")


# TC13 - Checkbox
try:
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Cricket']")
    checkbox.click()
    print("TC13 - PASS - Checkbox selected")
except:
    print("TC13 - FAIL")


# TC14 - Radio button
try:
    driver.find_element(By.XPATH, "//input[@type='radio' and @value='Male']").click()
    print("TC14 - PASS - Male selected")
except:
    print("TC14 - FAIL")


# TC15 - Dropdown
try:
    Select(driver.find_element(By.XPATH, "//select[@id='Skills']")).select_by_visible_text("Java")
    print("TC15 - PASS - Java selected")
except:
    print("TC15 - FAIL")


# TC16 - XPath index
try:
    driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
    print("TC16 - PASS - Second textbox found")
except:
    print("TC16 - FAIL")


# TC17 - Submit
try:
    driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Hariharan")
    driver.find_element(By.XPATH, "//textarea[contains(@ng-model,'Adress')]").send_keys("Chennai")
    driver.find_element(By.XPATH, "//input[contains(@ng-model,'Email')]").send_keys(
        "rohith" + str(random.randint(100000, 999999)) + "@gmail.com"
    )
    driver.find_element(By.XPATH, "//input[@ng-model='Phone']").send_keys(
        "9" + str(random.randint(100000000, 999999999))
    )
    driver.find_element(By.XPATH, "//input[@id='secondpassword']").send_keys("Selenium@123")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))).click()
    print("TC17 - PASS - Registration submitted")
except:
    print("TC17 - FAIL")


# TC18 - find_elements()
try:
    driver.get("https://demo.automationtesting.in/Register.html")
    inputs = driver.find_elements(By.XPATH, "//form[@id='basicBootstrapForm']//input")
    print("TC18 - PASS - Total inputs:", len(inputs))
except:
    print("TC18 - FAIL")


# TC19 - Dynamic element contains()
try:
    driver.find_element(By.XPATH, "//input[contains(@ng-model,'Email')]").send_keys("dynamic@gmail.com")
    print("TC19 - PASS - Dynamic element found")
except:
    print("TC19 - FAIL")


# TC20 - Complete registration
try:
    driver.get("https://demo.automationtesting.in/Register.html")

    driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Rohith")
    driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Hariharan")
    driver.find_element(By.XPATH, "//textarea[contains(@ng-model,'Adress')]").send_keys("Chennai")
    driver.find_element(By.XPATH, "//input[contains(@ng-model,'Email')]").send_keys("rohith@gmail.com")
    driver.find_element(By.XPATH, "//input[@ng-model='Phone']").send_keys("9876543210")
    driver.find_element(By.XPATH, "//input[@type='radio' and @value='Male']").click()
    driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Cricket']").click()
    Select(driver.find_element(By.XPATH, "//select[@id='Skills']")).select_by_visible_text("Java")
    driver.find_element(By.XPATH, "//input[@id='firstpassword']").send_keys("Selenium@123")
    driver.find_element(By.XPATH, "//input[@id='secondpassword']").send_keys("Selenium@123")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))).click()

    print("TC20 - PASS - Registration completed")

except:
    print("TC20 - FAIL")


print("==============================================")
print("ALL TEST CASES COMPLETED")
print("==============================================")

input("Press Enter to close browser...")
driver.quit()