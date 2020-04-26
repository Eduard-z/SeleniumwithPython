from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://test.salesforce.com/")
print(driver.title)  # title of the page

driver.get("https://google.com")
print(driver.title)  # title of the page

driver.back()
print(driver.title)  # title of the page

driver.forward()
print(driver.title)  # title of the page

driver.close()
