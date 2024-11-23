from car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if it meets the reliability test."""
        # Generate a random number between 0 and 100
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            # If the random number is less than reliability, drive as normal
            return super().drive(distance)
        else:
            # Otherwise, the car doesn't drive
            return 0
