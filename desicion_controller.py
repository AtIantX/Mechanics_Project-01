class DecisionController:

    def make_decision(self, car, intersection):
        initial_speed = car.initial_speed
        acceleration_positive = car.acceleration_positive
        acceleration_negative = car.acceleration_positive
        car_distance = car.initial_distance
        intersection_width = intersection.width
        yellow_light_duration = intersection.yellow_light_duration


