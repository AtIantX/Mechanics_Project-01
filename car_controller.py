from random import randrange


class CarController:

    def __init__(self):
        self.initial_speed_range = (20, 81)
        self.initial_distance_range = (10, 150)
        self.is_car_accelerating = True
        self.car_acceleration_positive_range = (1, 4)
        self.car_acceleration_negative_range = (1, 4)
        self.initial_speed = 0
        self.initial_distance = 0
        self.acceleration_positive = 0
        self.acceleration_negative = 0

    def get_variables_defined_random(self):
        self.initial_speed = randrange(*self.initial_speed_range)
        self.initial_distance = randrange(*self.initial_distance_range)
        self.acceleration_positive = randrange(*self.car_acceleration_positive_range)
        self.acceleration_negative = randrange(*self.car_acceleration_negative_range)
        self.initial_speed = randrange(*self.initial_speed_range)


