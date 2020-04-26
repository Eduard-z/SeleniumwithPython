from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()  # maximize window size

# driver.execute_script("window.scrollBy(0, 1000)", "")  # scroll down by pixel

flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[18]/td[1]/img')
# driver.execute_script("arguments[0].scrollIntoView();", flag)  # scroll down till the element is visible

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")  # scroll down till the end of the page
