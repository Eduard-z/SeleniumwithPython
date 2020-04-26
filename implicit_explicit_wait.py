from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")

driver.implicitly_wait(10)  # seconds

assert "Salesforce" in driver.title

driver.find_element_by_name("username").send_keys("ed@ed.ed")
driver.find_element_by_name("pw").send_keys("Cheglad3e/")
driver.find_element_by_name("Login").click()

time.sleep(10)

# explicit wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'save')))
element.click()

# driver.close()
