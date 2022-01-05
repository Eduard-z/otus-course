from src.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)
        self.name = __class__.__name__
