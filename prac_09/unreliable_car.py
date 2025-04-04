from prac_09.car import Car
from random import randint  # Or random.uniform(0, 100) if you want more precision

class UnreliableCar(Car):
    """An UnreliableCar that may not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with a reliability factor."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car.

        Only drive if random chance is below reliability.
        Return the actual distance driven.
        """
        random_chance = randint(0, 100)
        if random_chance < self.reliability:
            # Success: use parent class drive
            return super().drive(distance)
        else:
            # Failed to start
            return 0
