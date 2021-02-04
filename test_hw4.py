import unittest

from autotests import hw
class MyTestCase(unittest.TestCase) :
    def test_month(self, y=7):
        self.assertEqual('Summer','Summer')
        print(y)
    def test_month2(self, y=0):
        self.assertEqual('Wrong month number','Wrong month number')
        print(y)
    def test_month3(self, y=1):
        self.assertEqual(y, 1)
        print(y)
if __name__ == '__main__' :
    unittest.main()
