from design_patterns.builder.v1.domain.car import Car
from design_patterns.builder.v1.domain.director import Director

from design_patterns.builder.v1.domain.bus_builder import BusBuilder
from design_patterns.builder.v1.domain.jeep_builder import JeepBuilder

if __name__ == '__main__':
    # Builder - v1
    # Using a director to create instances of a car through a specific builder for each type
    director: Director = Director()

    print("===== Creating [Jeep] =====")
    jeep_builder: JeepBuilder = JeepBuilder()
    director.set_builder(builder=jeep_builder)

    jeep: Car = director.get_car()
    jeep.get_specification()

    print("\n===== Creating [Bus] =====")
    bus_builder: BusBuilder = BusBuilder()
    director.set_builder(builder=bus_builder)

    bus: Car = director.get_car()
    bus.get_specification()
