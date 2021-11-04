from abc import ABC, abstractmethod


class Figure(ABC):

    # Запретить создавать экземпляры базового класса Figure
    @abstractmethod
    # Если передана не геометрическая фигура, то нужно выбрасывать ошибку ValueError
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Wrong class instance given")
