from typing import List

from design_patterns.builder.v1.domain.car import Body, Engine, Wheel


class Builder:

    def get_wheels(self) -> List[Wheel]:
        pass

    def get_engine(self) -> Engine:
        pass

    def get_body(self) -> Body:
        pass
