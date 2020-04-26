from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")

element = driver.find_element_by_name("username")
print(element.is_displayed())  # returns true/false based on element's status
print(element.is_enabled())  # returns true/false

checkbox = driver.find_element_by_id("rememberUn")
print(checkbox.is_selected())  # returns true/false for radio-button, checkbox

driver.close()
