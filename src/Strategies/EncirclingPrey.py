import numpy as np

from src.Strategies.StrategySuperClass import StrategySuperClass
from src.utils.throw_coin import throwACoinBetween0to1


class EncirclingPrey(StrategySuperClass):
    def __init__(self, A_parameter):
        super().__init__()
        self.A_parameter = A_parameter

    def C(self):
        r_parameter = throwACoinBetween0to1()
        return 2 * r_parameter

    def calculateDistance(self, data_sample):
        C_parameter = self.C()
        return np.abs(C_parameter * self.Xstar - data_sample)

    def move(self, data_sample):
        distance = self.calculateDistance(data_sample)
        return self.Xstar - self.A_parameter * distance
