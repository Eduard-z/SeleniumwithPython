import unittest


def set_up_module():  # will be executed before executing any class or any method presented in the test-case
    print("setUpModule")


def tear_down_module():  # will be executed after completing everything presented in the python module
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:  # is executed before each test method
        print("This is login test")

    @classmethod
    def tearDown(self):  # is executed after each test method
        print("This is logout test")

    @classmethod
    def setUpClass(cls) -> None:  # is executed once the class is started
        print("Open the Application")

    @classmethod
    def tearDownClass(cls) -> None:  # is executed once the class is ended
        print("Close the Application")

    def test_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")


if __name__ == '__main__':
    unittest.main()
