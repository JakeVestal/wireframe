
import unittest
import math
from financier import Multiplication

class MultiplicationTestCase(unittest.TestCase):

    def setUp(self):
        self.multiplication = Multiplication(2)

    def test_zero(self):
        """Test 0 multiplied by 2"""

        # 0 multiplied by 2 return 0
        result = self.multiplication.multiply(0)
        self.assertEqual(result, 0)

    def test_natural_number(self):
        """Test natural number 5 multiplied by 2"""

        # 5 multiplied by 2 return 10
        result = self.multiplication.multiply(5)
        self.assertEqual(result, 10)

    def test_integer_number(self):
        """Test integer number -7 multiplied by 2"""

        # -7 multiplied by 2 return -14
        result = self.multiplication.multiply(-7)
        self.assertEqual(result, -14)

    def test_rational_number(self):
        """Test rational number 6/17 multiplied by 2"""

        # 6/17 multiplied by 2 return (6/17) * 2
        result = self.multiplication.multiply(6/17)
        self.assertEqual(result, (6/17) * 2)

    def test_real_number(self):
        """Test real number PI multiplied by 2"""

        # PI multiplied by 2 return 2PI
        result = self.multiplication.multiply(math.pi)
        self.assertEqual(result, math.pi * 2)


if __name__ == '__main__':
    unittest.main()

shorts_info = {'short_fees': [4,2,1,6,3], 'tax_diff': 38726}

def calc_market_portfolio(rf=0, tolerance=10**-3, shorts_info=False):

    if shorts_info is not None:
        new_returns = calc_short_returns(shorts_info)





