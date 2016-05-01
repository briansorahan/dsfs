import unittest
import linear_regression

class TestGetInterestRate(unittest.TestCase):
    def test_getInterestRate(self):
        self.assertEqual(linear_regression.getInterestRate('12.5%'), 12.5)

if __name__ == "__main__":
    unittest.main()
