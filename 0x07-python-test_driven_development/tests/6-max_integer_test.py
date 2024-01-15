#!/usr/bin/pyhton3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 0, 2, 1]), 5)
        self.assertEqual(max_integer([2, 4, 9, 6, 8]), 9)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
