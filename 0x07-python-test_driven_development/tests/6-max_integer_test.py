#!/usr/bin/python3
"""Unittest Module"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Function that test for integers"""

    def test_max_integer(self):
        """Test cases"""

        self.assertEqual(max_integer([5, 8, 7]), 8)
        self.assertEqual(max_integer([-99, -54, -10675, 2]), 2)
        self.assertEqual(max_integer([13, -2, -1, -9]), 13)
        self.assertEqual(max_integer([-17, 22, 64]), 64)
        self.assertEqual(max_integer([-11, -22, -9]), -9)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([13, -106]), 13)
        self.assertEqual(max_integer([2, 26, 9]), 26)
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
