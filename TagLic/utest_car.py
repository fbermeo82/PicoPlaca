from unittest import TestCase
from TagLic import Car as cr

__author__ = "Franz Bermeo Quezada"
__version__ = "1.0"
__email__ = "franz.bermeo@gmail.com"

class TestCar(TestCase):
    def utest_negative(self):
        c = cr.Car()
        self.assertRaises(Exception, c.getYear)

    def test_getTag(self):
        self.fail()

    def test_setYear(self):
        self.fail()
