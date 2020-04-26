from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
driver.get("https://catalog.onliner.by/")
driver.maximize_window()

flats = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/header/div[1]/div/nav/ul[1]/li[4]/a')
minsk = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/header/div[1]/div/nav/ul[1]/li[4]/div/div/div/div/div[1]/div[2]/div/div[1]/ul/li[1]/a')

# hover an element
hovering = ActionChains(driver)
hover1 = hovering.move_to_element(flats).perform()
time.sleep(3)
hovering.move_to_element(minsk).click().perform()

# double-click a button
driver.get("http://testautomationpractice.blogspot.com/")

copy_text = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button')

doubleclick = ActionChains(driver)
doubleclick.double_click(copy_text).perform()
time.sleep(3)

# right-click a button (just an example)
doubleclick.context_click(copy_text).perform()
time.sleep(3)

# drag-and-drop an element
source_element = driver.find_element_by_xpath('//*[@id="draggable"]')
target_element = driver.find_element_by_xpath('//*[@id="droppable"]')

drag_drop = ActionChains(driver)
drag_drop.drag_and_drop(source_element, target_element).perform()
