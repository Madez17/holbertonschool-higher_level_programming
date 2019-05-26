#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
  def test_max(self):
      self.assertEqual(max_integer([3, 29, 9]), 29)  
  def test_max_negative_positive(self):
      self.assertEqual(max_integer([0, -29, -9]), 0) 
  def test_max_negative(self):
      self.assertEqual(max_integer([-3, -29, -4]), -3)
  def test_zero(self):
      self.assertEqual(max_integer([0, 0, 0]), 0)
  def test_float(self):
      self.assertEqual(max_integer([2.4, 4.5, 6.5]), 6.5)
  def test_negative(self):
      self.assertAlmostEqual(max_integer([-1]), -1)
  def test_empty_list(self):
      self.assertEqual(max_integer([]), None)
  def test_empty(self):
      self.assertEqual(max_integer(), None)
  
  
if __name__ == '__main__':
    unittest.main()
