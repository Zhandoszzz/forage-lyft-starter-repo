import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        tire = CarriganTire([0.1, 0.5, 0.8, 0.9])
        self.assertTrue(tire.needs_service())

    def test_battery_should_not_be_serviced(self):
        tire = CarriganTire([0.1, 0.5, 0.8, 0.7])
        self.assertFalse(tire.needs_service())
