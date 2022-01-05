import pytest

side_length1 = 11
side_length2 = 6
side_length3 = 13
side_length4 = 3
side_length_square1 = 4


def test_create_instance(rectangle1):
    """Check instance attributes"""
    assert rectangle1.side_A == side_length1
    assert rectangle1.side_B == side_length2
    assert rectangle1.name == "Rectangle"
    assert rectangle1.perimeter == (side_length1 + side_length2) * 2
    assert rectangle1.area == side_length1 * side_length2


def test_add_area(rectangle1, rectangle2):
    """Sum of areas of 2 rectangles"""
    assert rectangle1.add_area(rectangle2) == side_length1 * side_length2 + side_length3 * side_length4


def test_add_area_figure(rectangle1, square1):
    """Sum of areas of a rectangle and another figure"""
    assert rectangle1.add_area(square1) == side_length1 * side_length2 + side_length_square1 ** 2


def test_add_area_not_figure(rectangle2, car):
    """Sum of areas of a rectangle and non-Figure"""
    with pytest.raises(ValueError):
        rectangle2.add_area(car)
