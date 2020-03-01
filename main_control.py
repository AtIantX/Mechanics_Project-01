from car_controller import CarController
from intersection_controller import IntersectionController


class MainControl:

    def __init__(self):
        # Create Car
        self.car = CarController()
        self.intersection = IntersectionController()

    # @staticmethod
    def define_variables(self):
        self.car.get_variables_defined_random()
        self.intersection.get_variables_defined_random()


if __name__ == "__main__":
    control = MainControl()
    control.define_variables()
