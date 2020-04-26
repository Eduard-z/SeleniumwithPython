from selenium import webdriver
import time

fp = webdriver.FirefoxProfile()  # the ability to specify a download path and other options
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "test/plain, application/pdf")  # mime-type
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\\Users\zakharove\Downloads")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path="C:/Users\zakharove\drivers\geckodriver.exe", firefox_profile=fp)

# download a file
driver.get("https://www.rstqb.org/ru/istqb-downloads.html")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="article-2254"]/div[2]/ul/li[2]/a').click()  # download link
time.sleep(5)  # wait until file is downloaded
