# install allure-pytest package
# launch from terminal pytest -v -s --alluredir=Pytest_package/allure_reports Pytest_package/test_pytest_allure.py

"""

install Allure commandline application

convert allure report into html format - run in cmd:
C:\Users\zakharove\PycharmProjects\SeleniumwithPython\Pytest_package\allure_reports\allure_into_html>
allure generate C:\Users\zakharove\PycharmProjects\SeleniumwithPython\Pytest_package\allure_reports -
where template is target_folder>allure generate source_folder

convert allure report into html format into temporary folder - run in cmd:
C:\Users\zakharove\PycharmProjects\SeleniumwithPython\Pytest_package\allure_reports\allure_into_html>
allure serve C:\Users\zakharove\PycharmProjects\SeleniumwithPython\Pytest_package\allure_reports -
where template is any_folder>allure serve source_folder
"""

import pytest


@pytest.fixture()  # executes setup method before certain methods
def setup():
    print("Once before every method")


@pytest.yield_fixture()  # executes setup2 method before & after certain methods
def setup2():
    print("Before every method")  # before
    yield
    print("After every method")  # after


def testmethod1(setup):
    print("testmethod1")


def testmethod2(setup2):
    print("testmethod2")
