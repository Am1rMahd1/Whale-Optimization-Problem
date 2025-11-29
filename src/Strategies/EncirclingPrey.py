from src.Strategies.StrategySuperClass import StrategySuperClass
from src.utils.throw_coin import throwACoinBetween0to1
import numpy as np


class EncirclingPrey(StrategySuperClass):
    def __init__(self, A_parameter):
        super().__init__(A_parameter)
        self.A_parameter = A_parameter


    def C(self):
        probability = throwACoinBetween0to1()
        return 2 * probability

    def calculateDistance(self, data_sample):
        C_parameter = self.C()
        return np.abs(C_parameter * self.Xstar - data_sample)

    def move(self, data_sample):
        distance = self.calculateDistance(data_sample)
        return self.Xstar - self.A_parameter * distance
