from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.name = __class__.__name__
        self.side_A = a
        self.side_B = b
        self.side_C = c

    # если треугольник создать нельзя, то класс должен вернуть None
    def __new__(cls, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            return None
        return super().__new__(cls)

    @property
    def perimeter(self):
        return self.side_A + self.side_B + self.side_C

    @property
    def area(self):
        s = self.perimeter / 2
        return (s * (s - self.side_A) * (s - self.side_B) * (s - self.side_C)) ** 0.5

    def add_area(self, figure):
        super().add_area(figure)
        return self.area + figure.area
