import unittest
import numpy as np

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

class TestTrueFunction(unittest.TestCase):

    def test_x_0(self):
        x = 0.0
        expected_y = 0.0
        result_y = true_function(x)
        self.assertAlmostEqual(result_y, expected_y)

if __name__ == '__main__':
    unittest.main()
