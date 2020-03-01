from car_controller import CarController
from intersection_controller import IntersectionController
from desicion_controller import DecisionController


class MainControl:

    def __init__(self):
        # Create Car
        self.car = CarController()
        self.intersection = IntersectionController()
        self.decision_controller = DecisionController()

    # @staticmethod
    def define_variables(self):
        self.car.get_variables_defined_random()
        self.intersection.get_variables_defined_random()

    def make_decision(self):
        self.decision_controller.make_decision(car=self.car, intersection=self.intersection)


if __name__ == "__main__":
    control = MainControl()
    control.define_variables()
    control.make_decision()

