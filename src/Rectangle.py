from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.name = __class__.__name__
        self.side_A = a
        self.side_B = b

    @property
    def perimeter(self):
        return (self.side_A + self.side_B) * 2

    @property
    def area(self):
        return self.side_A * self.side_B

    def add_area(self, figure):
        super().add_area(figure)
        return self.area + figure.area
