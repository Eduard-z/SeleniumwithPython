from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Firefox(executable_path="C:/Users\zakharove\drivers\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:/Users\zakharove\drivers\IEDriverServer.exe")
driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")
print(driver.title)  # title of the page
print(driver.current_url)  # return the URL of the page

driver.find_element_by_xpath('//*[@id="username"]').clear()
driver.find_element_by_name("username").send_keys("ed@ed.ed")
driver.find_element_by_name("pw").clear()
driver.find_element_by_name("pw").send_keys("Cheglad3e/")
driver.find_element_by_name("Login").click()
time.sleep(10)

# driver.close()  # close currently focused browser
# driver.quit()  # close all the browsers
