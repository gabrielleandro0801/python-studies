from typing import Any

from design_patterns.factory.v1.services.shape_service import Shape, Square, Rectangle


class ShapeFactory:

    def create_shape(self, name) -> Shape:
        options: dict = {
            'square': ShapeFactory.create_square,
            'rectangle': ShapeFactory.create_rectangle,
        }

        factory: Any = options.get(name)
        if factory is not None:
            return factory()

        raise NotImplementedError

    @classmethod
    def create_square(cls) -> Shape:
        width = 10
        return Square(width)

    @classmethod
    def create_rectangle(cls) -> Shape:
        height = 10
        width = 5
        return Rectangle(height, width)
