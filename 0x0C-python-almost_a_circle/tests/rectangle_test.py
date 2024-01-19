#!/usr/bin/python3
''' Unittest for rectangle class
and its modules'''

import unittest
Base = __import__('base.py').Base

class TestShapes(unittest.TestCase):
    def test_base(self):
        a = Base()
        self.assertEqual(print(a.id), 1)

if __name__ == '__main__':
    unittest.main()
