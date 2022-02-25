from design_patterns.factory.v1.factories.shape_factory import ShapeFactory
from design_patterns.factory.v1.services.shape_service import Shape


def main(factory: ShapeFactory, name: str) -> None:
    try:
        shape: Shape = factory.create_shape(name)
    except NotImplementedError:
        print(f'Shape: [{name}] not implemented\n')
    else:
        print(f'Shape: [{name}] | Area: [{shape.calculate_area()}] | Perimeter: [{shape.calculate_perimeter()}]\n')


if __name__ == '__main__':
    # Factory - v1
    # Using a factory to instantiate a class single and abstract the way it is created
    shape_factory: ShapeFactory = ShapeFactory()

    main(shape_factory, 'square')
    main(shape_factory, 'circle')
    main(shape_factory, 'rectangle')
