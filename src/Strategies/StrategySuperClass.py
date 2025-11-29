from abc import ABC, abstractmethod


class StrategySuperClass(ABC):
    def __init__(self, A_parameter):
        pass

    def setXstar(self, Xstar):
        self.Xstar = Xstar
        return self

    @abstractmethod
    def calculateDistance(self, data_sample):
        pass

    @abstractmethod
    def move(self, data_sample):
        pass
