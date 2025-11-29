import numpy as np
def throwACoinBetween0to1():
    probability = np.random.random_sample()
    return round(probability, 2)
