#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
  def test_upper(self):
      self.assertEqual(max_integer([3, 29, 9]), 29)  

if __name__ == '__main__':
    unittest.main()
