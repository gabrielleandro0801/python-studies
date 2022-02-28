from typing import List

from design_patterns.builder.v1.domain.builder import Builder
from design_patterns.builder.v1.domain.car import Body, Engine, Wheel


class JeepBuilder(Builder):
    def __init__(self):
        self.__wheels: List[Wheel] = []
        self.__engine: Engine = Engine()
        self.__body: Body = Body()

    def get_wheels(self) -> List[Wheel]:
        for _ in range(0, 4):
            wheel: Wheel = Wheel()
            wheel.size = 22
            self.__wheels.append(wheel)
        return self.__wheels

    def get_engine(self) -> Engine:
        self.__engine.horsepower = 400
        return self.__engine

    def get_body(self) -> Body:
        self.__body.shape = "SUV"
        return self.__body
