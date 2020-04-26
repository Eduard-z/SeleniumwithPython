from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")

# capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies have been created
print(cookies)  # print all cookie pairs

# add new cookie to the browser
cookie = {'name': 'MyCookie', 'value': '0123654789'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies after adding new cookie
print(cookies)  # print all cookie pairs

# delete a cookie
driver.delete_cookie('MyCookie')

time.sleep(5)
cookies = driver.get_cookies()
print(len(cookies))  # print number of cookies after deleting a cookie --> not changed because new cookie was generated
print(cookies)  # print all cookie pairs

# delete all cookies
driver.delete_all_cookies()  # delete all cookies
cookies = driver.get_cookies()
print(len(cookies))  # 0
