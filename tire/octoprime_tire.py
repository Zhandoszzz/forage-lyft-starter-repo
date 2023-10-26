from tire.tire import Tire
import random


class OctoprimeTire(Tire):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        return sum(self.tires) >= 3
