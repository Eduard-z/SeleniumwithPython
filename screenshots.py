from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://login.salesforce.com/")

# driver.save_screenshot(r"C:\Users\zakharove\Desktop\KanbanAddToLongList.png")  # method 1
driver.get_screenshot_as_file(r"C:\Users\zakharove\Desktop\KanbanAddToLongList.png")  # method 2
