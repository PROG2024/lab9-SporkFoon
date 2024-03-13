"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import math
import pytest

def test_add_area_typical():
    circle1 = Circle(3)
    circle2 = Circle(4)
    result_circle = circle1.add_area(circle2)
    expected_radius = math.hypot(3, 4)
    assert result_circle.get_radius() == expected_radius, "The resulting circle does not have the correct radius."
    expected_area = math.pi * expected_radius ** 2
    assert math.isclose(result_circle.get_area(), expected_area), "The resulting circle does not have the correct area."

def test_add_area_edge_zero_radius():
    circle_zero = Circle(0)
    circle_non_zero = Circle(4)
    result_circle_from_zero = circle_zero.add_area(circle_non_zero)
    result_circle_to_zero = circle_non_zero.add_area(circle_zero)
    assert result_circle_from_zero.get_radius() == 4, "The resulting circle's radius is incorrect when starting from zero radius."
    assert result_circle_to_zero.get_radius() == 4, "The resulting circle's radius is incorrect when adding to zero radius."
    expected_area = math.pi * 4 ** 2
    assert math.isclose(result_circle_from_zero.get_area(), expected_area), "The resulting circle's area is incorrect when starting from zero radius."
    assert math.isclose(result_circle_to_zero.get_area(), expected_area), "The resulting circle's area is incorrect when adding to zero radius."

def test_circle_negative_radius_exception():
    with pytest.raises(ValueError) as e:
        _ = Circle(-1)
    assert str(e.value) == "radius must be non-negative", "Creating a circle with a negative radius should raise ValueError."
