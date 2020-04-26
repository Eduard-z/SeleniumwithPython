"""
Run a specific test, method or package:
in Terminal: pytest -v -s Pytest_package/test_pytest_fixtures.py
in Terminal: pytest -v -s Pytest_package/test_pytest_fixtures.py::testmethod2
in Terminal: pytest -v -s Pytest_package
-s to print statements
-v to verbose
--tb=line only one line per failure
"""

# to get HTML reports:
# pip install pytest-html and
# launch from terminal pytest -v -s --html=Pytest_package/report.html Pytest_package/test_pytest_fixtures.py
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
