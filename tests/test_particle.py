import unittest
from src.particle import Carrier
from src.field import ElectricField

class TestCarrier(unittest.TestCase):
    def test_motion_electron(self):
        field = ElectricField(1.0)
        e = Carrier('electron', 0.0, 0.0)
        e.move(field, 1.0)
        self.assertLess(e.positon, 0.0) #electron moves in neg direction

    def test_motion_hole(self):
        field = ElectricField(1.0)
        e = Carrier('hole', 0.0, 0.0)
        e.move(field, 1.0)
        self.assertGreater(e.positon, 0.0)