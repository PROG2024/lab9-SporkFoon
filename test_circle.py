"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import pytest
from circle import Circle
import math

def test_add_area_typical():
    circle1 = Circle(3)
    circle2 = Circle(4)
    result_circle = circle1.add_area(circle2)
    expected_radius = math.hypot(3, 4)
    assert result_circle.get_radius() == expected_radius
    assert math.isclose(result_circle.get_area(), math.pi * expected_radius ** 2)

def test_add_area_edge():
    circle_zero = Circle(0)
    circle_non_zero = Circle(4)
    result_circle1 = circle_zero.add_area(circle_non_zero)
    result_circle2 = circle_non_zero.add_area(circle_zero)
    expected_radius = 4
    assert result_circle1.get_radius() == expected_radius
    assert math.isclose(result_circle1.get_area(), math.pi * expected_radius ** 2)
    assert result_circle2.get_radius() == expected_radius
    assert math.isclose(result_circle2.get_area(), math.pi * expected_radius ** 2)

def test_circle_negative_radius_exception():
    with pytest.raises(ValueError):
        Circle(-1)