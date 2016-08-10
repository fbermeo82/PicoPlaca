__author__ = "Franz Bermeo Quezada"
__version__ = "1.0"
__email__ = "franz.bermeo@gmail.com"

class Car:
    def __init__(self, _year, _model, _tag):
        self.year = _year
        self.model = _model
        self.tag = _tag

    @property
    def getYear(self):
        return self.year

    @property
    def getTag(self):
        return self.tag

    @property
    def getModel(self):
        return self.model

    def setYear(self, value):
        self.year = value

    def setTag(self, value):
        self.tag = value

    def setModel(self, value):
        self.model = value