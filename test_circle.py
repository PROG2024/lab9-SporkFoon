"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):
	def test_add_area(self):
		c1 = Circle(3)
		c2 = Circle(4)
		result_circle = c1.add_area(c2)
		expected_rad = math.hypot(3, 4)
		self.assertEqual(result_circle.get_radius(), expected_rad)
		self.assertAlmostEqual(result_circle.get_area(), math.pi * expected_rad ** 2)

	def test_add_area_zero(self):
		c0 = Circle(0)
		c_non_0 = Circle(4)
		result_c1 = c0.add_area(c_non_0)
		result_c2 = c_non_0.add_area(c0)
		expected_rad = 4
		self.assertEqual(result_c1.get_radius(), expected_rad)
		self.assertAlmostEqual(result_c1.get_area(), math.pi * expected_rad ** 2)
		self.assertEqual(result_c2.get_radius(), expected_rad)
		self.assertAlmostEqual(result_c2.get_area(), math.pi * expected_rad ** 2)

	def test_negative_radius(self):
		with self.assertRaises(ValueError):
			c = Circle(-1)

if __name__ == '__main__':
    unittest.main()
    