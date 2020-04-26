from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_element_by_id("signup_link").click()

employees = driver.find_element_by_id("signup_form_1-CompanyEmployees")
drp = Select(employees)
# select by visible text
drp.select_by_visible_text('21 - 200 employees')

country = driver.find_element_by_id("signup_form_1-CompanyCountry")
drp = Select(country)
# select by value/index
drp.select_by_value('DZ')  # drp.select_by_index(4)

print(len(drp.options))  # count number of options
# capture all the options
all_options = drp.options
for option in all_options:
    print(option.text)

# count number of links
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

driver.find_element(By.LINK_TEXT, 'Privacy Statement').click()
