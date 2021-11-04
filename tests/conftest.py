import pytest
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Circle import Circle


@pytest.fixture
def square1():
    square1 = Square(a=4)
    yield square1


@pytest.fixture
def square2():
    square2 = Square(a=7)
    yield square2


@pytest.fixture
def rectangle1():
    rectangle1 = Rectangle(a=11, b=6)
    yield rectangle1


@pytest.fixture
def rectangle2():
    rectangle2 = Rectangle(a=13, b=3)
    yield rectangle2


@pytest.fixture
def triangle1():
    triangle1 = Triangle(a=4, b=7, c=10)
    yield triangle1


@pytest.fixture
def triangle2():
    triangle2 = Triangle(a=16, b=11, c=22)
    yield triangle2


@pytest.fixture
def circle1():
    circle1 = Circle(r=4)
    yield circle1


@pytest.fixture
def circle2():
    circle2 = Circle(r=7)
    yield circle2


@pytest.fixture
def car():
    class Car:
        def __init__(self):
            self.area = 23

    yield Car()
