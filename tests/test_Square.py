import pytest

side_length1 = 4
side_length2 = 7
side_length_triangle1 = 4
side_length_triangle2 = 7
side_length_triangle3 = 10


def test_create_instance(square1):
    """Check instance attributes"""
    assert square1.side_A == side_length1
    assert square1.side_B == side_length1
    assert square1.name == "Square"
    assert square1.perimeter == side_length1 * 4
    assert square1.area == side_length1 ** 2


def test_add_area(square1, square2):
    """Sum of areas of 2 squares"""
    assert square1.add_area(square2) == side_length1 ** 2 + side_length2 ** 2


def test_add_area_figure(square1, triangle1):
    """Sum of areas of a square and another figure"""
    s = (side_length_triangle1 + side_length_triangle2 + side_length_triangle3) / 2
    assert square1.add_area(triangle1) == side_length1 ** 2 + \
           (s * (s - side_length_triangle1) * (s - side_length_triangle2) * (s - side_length_triangle3)) ** 0.5


def test_add_area_not_figure(square2, car):
    """Sum of areas of a square and non-Figure"""
    with pytest.raises(ValueError):
        square2.add_area(car)
