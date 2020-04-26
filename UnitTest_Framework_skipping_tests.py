import unittest


class SkipTests(unittest.TestCase):
    @unittest.SkipTest  # decorator
    def test_1(self):
        print(self._testMethodName)

    @unittest.skip("Skipping this test-case as it is not ready yet")
    def test_2(self):
        print(self._testMethodName)

    @unittest.skipIf(1 == 1, "Skip if condition is not true")
    def test_3(self):
        print(self._testMethodName)

    def test_4(self):
        print(self._testMethodName)

    def test_5(self):
        print(self._testMethodName)


if __name__ == '__main__':
    unittest.main()
