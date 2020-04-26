from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()  # the ability to specify a download path
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\\Users\zakharove\Downloads"})

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe", options=chromeOptions)
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)  # "RESULT_FileUpload-11" element is located inside the frame

# upload a file
driver.find_element_by_id("RESULT_FileUpload-11").send_keys(r"C:\Users\zakharove\ownCloud\Documents\files\dog 216.3.jpg")
time.sleep(3)

# download a file
driver.get("https://www.rstqb.org/ru/istqb-downloads.html")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="article-2254"]/div[2]/ul/li[1]/a').click()  # download link
time.sleep(5)  # wait until file is downloaded
