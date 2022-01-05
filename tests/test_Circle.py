import math
import pytest

radius1 = 4
radius2 = 7
side_length_rectangle1 = 11
side_length_rectangle2 = 6


def test_create_instance(circle1):
    """Check instance attributes"""
    assert circle1.radius == radius1
    assert circle1.name == "Circle"
    assert circle1.perimeter == radius1 * math.pi * 2
    assert circle1.area == math.pi * radius1 ** 2


def test_add_area(circle1, circle2):
    """Sum of areas of 2 circles"""
    assert circle1.add_area(circle2) == math.pi * radius1 ** 2 + math.pi * radius2 ** 2


def test_add_area_figure(circle1, rectangle1):
    """Sum of areas of a circle and another figure"""
    assert circle1.add_area(rectangle1) == math.pi * radius1 ** 2 + side_length_rectangle1 * side_length_rectangle2


def test_add_area_not_figure(circle2, car):
    """Sum of areas of a circle and non-Figure"""
    with pytest.raises(ValueError):
        circle2.add_area(car)
