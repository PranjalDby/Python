import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,12),22)
        self.assertEqual(calc.add(-1,0),-1)
        self.assertEqual(calc.add(-1,-2),-3)
        
    def test_divide(self):
        res = calc.divide(-10,1)
        self.assertEqual(res,-10)
        with self.assertRaises(ValueError):
            calc.divide(10,0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,2),20)


if __name__ == "__main__":
    unittest.main()