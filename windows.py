from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")

driver.find_element_by_id("privacy-link").click()
print(driver.current_window_handle)  # CDwindow-4FE1AE218DE0421EE4734F3F12FAA963 - parent

handles = driver.window_handles  # returns all the handle values of all opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title, handle)

    if driver.title == "Login | Salesforce":  # close the window
        driver.close()
