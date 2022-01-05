import pytest
import math
from src.Triangle import Triangle

side_length1 = 4
side_length2 = 7
side_length3 = 10
side_length4 = 16
side_length5 = 11
side_length6 = 22
radius_circle1 = 4


def test_create_instance(triangle1):
    """Check instance attributes"""
    assert triangle1.side_A == side_length1
    assert triangle1.side_B == side_length2
    assert triangle1.side_C == side_length3
    assert triangle1.name == "Triangle"
    assert triangle1.perimeter == side_length1 + side_length2 + side_length3
    s = (side_length1 + side_length2 + side_length3) / 2
    assert triangle1.area == (s * (s - side_length1) * (s - side_length2) * (s - side_length3)) ** 0.5


def test_add_area(triangle1, triangle2):
    """Sum of areas of 2 triangles"""
    s1 = (side_length1 + side_length2 + side_length3) / 2
    s2 = (side_length4 + side_length5 + side_length6) / 2
    assert triangle1.add_area(triangle2) == (
            s1 * (s1 - side_length1) * (s1 - side_length2) * (s1 - side_length3)) ** 0.5 + (
                   s2 * (s2 - side_length4) * (s2 - side_length5) * (s2 - side_length6)) ** 0.5


def test_add_area_figure(triangle1, circle1):
    """Sum of areas of a triangle and another figure"""
    s = (side_length1 + side_length2 + side_length3) / 2
    assert triangle1.add_area(circle1) == \
           (s * (s - side_length1) * (s - side_length2) * (s - side_length3)) ** 0.5 + math.pi * radius_circle1 ** 2


def test_add_area_not_figure(triangle2, car):
    """Sum of areas of a triangle and non-Figure"""
    with pytest.raises(ValueError):
        triangle2.add_area(car)


def test_sum_of_two_sides_equal_to_third():
    """Sum of 2 sides equals to the third side length"""
    triangle3 = Triangle(a=5, b=6, c=11)
    assert triangle3 is None


def test_sum_of_two_sides_less_than_third():
    """Sum of 2 sides is less than the third side length"""
    triangle4 = Triangle(a=5, b=6, c=12)
    assert triangle4 is None
