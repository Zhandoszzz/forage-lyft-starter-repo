import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        tire = OctoprimeTire([0.8, 0.5, 0.8, 0.9])
        self.assertTrue(tire.needs_service())

    def test_battery_should_not_be_serviced(self):
        tire = OctoprimeTire([0.1, 0.5, 0.8, 0.7])
        self.assertFalse(tire.needs_service())
