from typing import List


class Car:
    def __init__(self):
        self.__wheels: List[Wheel] = []
        self.__engine: Engine = None
        self.__body: Body = None

    def set_body(self, body) -> None:
        self.__body = body

    def set_wheels(self, wheels) -> None:
        self.__wheels = wheels

    def set_engine(self, engine) -> None:
        self.__engine = engine

    def get_specification(self) -> None:
        print(f'Body [{self.__body.shape}]')
        print(f'Engine horsepower [{self.__engine.horsepower}]')
        list(map(lambda wheel: print(f'Tire size [{wheel.size}]'), self.__wheels))


# Car parts
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None
