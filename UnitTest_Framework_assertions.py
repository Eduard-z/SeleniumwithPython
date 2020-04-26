import unittest
from selenium import webdriver


class TestAssert(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        self.title_of_the_page = self.driver.title

        self.assertEqual("Google", self.title_of_the_page, "titles are not same")  # if both parameters match - passed
        self.assertTrue(self.title_of_the_page == "Google", "expression is false")  # if the expression is true - passed

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users\zakharove\drivers\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        self.title_of_the_page = self.driver.title

        self.assertNotEqual("Bing1", self.title_of_the_page, "titles are same")  # if both parameters differ - passed
        self.assertFalse(self.title_of_the_page == "Bing1", "expression is true")  # if the expression is false - passed

    def test_None(self):
        value1 = 1
        valueNone = None
        self.assertIsNone(valueNone, "valueNone is not None")  # if the value or expression is None - passed
        self.assertIsNotNone(value1, "value1 is None")  # if the value or expression is not None - passed

    def test_contains(self):
        sequence = ["a", "b", "c"]
        self.assertIn("a", sequence, "'a' is not in the list")  # if the 2nd element contains the 1st element - passed
        self.assertNotIn("d", sequence, "'d' is in the list")  # if the 2nd element doesn't contain the 1st one - passed

    def test_comparison(self):
        self.assertGreater(10, 9)  # if the 1st value is greater than the 2nd value - passed
        self.assertGreaterEqual(10,10)  # if the 1st value is greater than or equal to the 2nd value - passed
        self.assertLess(10, 11)  # if the 1st value is lesser than the 2nd value - passed
        self.assertLessEqual(10,10)  # if the 1st value is lesser than or equal to the 2nd value - passed


if __name__ == '__main__':
    unittest.main()
