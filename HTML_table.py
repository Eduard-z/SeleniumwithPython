from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

# count number of rows (truncate "[index]" of xpath)
rows = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr'))
# count number of columns (truncate "[index]" of xpath)
columns = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th'))

# print table elements
for r in range(2, rows+1):
    for c in range(1, columns+1):
        val = driver.find_element_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
        print(val, end='    ')
    print()
