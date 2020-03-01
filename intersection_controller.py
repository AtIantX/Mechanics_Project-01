from random import randrange


class IntersectionController:

    def __init__(self):
        self.intersection_width_range = (5, 21)
        self.yellow_light_duration_range = (2, 6)
        self.width = 0
        self.yellow_light_duration = 0

    def get_variables_defined_random(self):
        self.width = randrange(*self.intersection_width_range)
        self.yellow_light_duration = randrange(*self.yellow_light_duration_range)
