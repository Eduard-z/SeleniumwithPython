import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentindollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_paymentineuro(self):
        print("This is payment in euro test")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
