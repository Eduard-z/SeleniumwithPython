from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/")

driver.switch_to.frame('packageListFrame')  # first frame (by name or by index)
driver.find_element_by_link_text('org.openqa.selenium').click()

time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')  # second frame
driver.find_element_by_link_text('WebDriver').click()

time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame('classFrame')  # third frame
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]').click()
