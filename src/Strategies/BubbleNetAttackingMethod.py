import numpy as np

from Strategies.StrategySuperClass import StrategySuperClass


class BubbleNetAttackingMethod(StrategySuperClass):
    def __init__(self):
        super().__init__()
        self.b = 1

    def calculateDistance(self, data_sample):
        return np.abs(self.Xstar - data_sample)

    def move(self, data_sample):
        D = self.calculateDistance(data_sample)
        # todo: what is l parameter?
        l = self.l()
        # todo: what is b parameter?
        b = self.b
        return D * np.exp(b * l) * np.cos(2 * np.pi * l) + self.Xstar

    def l(self):
        return np.random.uniform(low=-1, high=1)

    def set_b(self, b_parameter):
        self.b = b_parameter
        return self
