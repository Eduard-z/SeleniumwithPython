# creating and running test-suites
import unittest
from Package_1.TC_LoginTest import LoginTest
from Package_1.TC_SignupTest import SignupTest

from Package_2.TC_PaymentTest import PaymentTest
from Package_2.TC_PaymentReturnTest import PaymentReturnTest

# get all tests from test-classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# creating test-suites
sanity_test_suite = unittest.TestSuite([tc1, tc2])  # test-suite includes tc1 and tc2 test-cases
functional_test_suite = unittest.TestSuite([tc3, tc4])  # test-suite includes tc3 and tc4 test-cases

unittest.TextTestRunner(verbosity=2).run(sanity_test_suite)  # executes sanity_test_suite
