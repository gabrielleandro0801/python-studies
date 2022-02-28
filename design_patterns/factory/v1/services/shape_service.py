from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> int or float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> int or float:
        pass


class Square(Shape):
    def __init__(self, width):
        self.__width = width

    def calculate_area(self) -> int or float:
        return self.__width ** 2

    def calculate_perimeter(self) -> int or float:
        return 4 * self.__width


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self) -> int or float:
        return self.__height * self.__width

    def calculate_perimeter(self) -> int or float:
        return 2 * (self.__height + self.__width)
