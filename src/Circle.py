import math
from src.Figure import Figure


class Circle(Figure):

    def __init__(self, r):
        self.name = __class__.__name__
        self.radius = r

    @property
    def perimeter(self):
        return self.radius * math.pi * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def add_area(self, figure):
        super().add_area(figure)
        return self.area + figure.area
