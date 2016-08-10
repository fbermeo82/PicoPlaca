from unittest import TestCase
from TagLic import Validator as vl

__author__ = "Franz Bermeo Quezada"
__version__ = "1.0"
__email__ = "franz.bermeo@gmail.com"

class TestValidator(TestCase):
    def utest_negative(self):
        v = vl.Validator()
        self.assertRaises(Exception, v.HasRestrictedTransit('10/08/2016', '08-30','AYC-3798'))

    def test_digit_validator(self):
        self.fail()

    def test_isDateFormat(self):
        self.fail()

    def test_HasRestrictedTransit(self):
        self.fail()
