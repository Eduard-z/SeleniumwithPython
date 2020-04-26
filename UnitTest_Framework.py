# pip install html-testRunner
import HtmlTestRunner
import unittest
from selenium import webdriver


class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page is: " + self.driver.title)

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page is: " + self.driver.title)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="unittest_HTML_Reports"))
# to get HTML reports launch from terminal (python UnitTest_Framework.py)
