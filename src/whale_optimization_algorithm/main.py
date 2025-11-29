import numpy as np
import plotly.express as px

from src.Strategies.BubbleNetAttackingMethod import BubbleNetAttackingMethod
from src.Strategies.EncirclingPrey import EncirclingPrey
from src.Strategies.SearchForPrey import SearchForPrey


def create_data(distribution, how_many, dimensional):
    if distribution == "uniform":
        return np.random.uniform(size=(how_many, dimensional))
    elif distribution == "normal":
        return np.random.normal(size=(how_many, dimensional))


# we consider that our problem is 1-dimensional
def F(x):
    return x**2


def calculateFitnessForAllData(data):
    x_dimensional_of_the_data = data
    return F(x_dimensional_of_the_data)


def findTheXStarIndex(fitnessVector):
    return np.argmin(fitnessVector)


def chooseMovementStrategyRandomly(probability, A_parameter):
    if probability >= 0.5:
        if np.abs(A_parameter) < 1:
            return EncirclingPrey()
        else:
            return SearchForPrey()
    else:
        return BubbleNetAttackingMethod()


def throwACoinBetween0to1():
    probability = np.random.random_sample()
    return round(probability, 2)


def a(iteration_number, max_iteration):
    # -2/max * t + 2
    return 2 - iteration_number * 2 / max_iteration


def A(a_parameter):
    r = throwACoinBetween0to1()
    return 2 * a_parameter * r - a_parameter


def whaleOptimizationAlgorithm(data, max_iteration):
    # make a copy of original data
    data = data.copy()
    for iteration_number in range(max_iteration):
        fitnessVector = calculateFitnessForAllData(data)

        x_star_index = findTheXStarIndex(fitnessVector)

        x_star_value = data[x_star_index]

        for data_samples in data:
            probability = throwACoinBetween0to1()

            # a parameter is a number that is reducing from 2 to 0 during iterations
            a_parameter = a(iteration_number, max_iteration)

            A_parameter = A(a_parameter)

            movementObject = chooseMovementStrategyRandomly(probability, A_parameter)

        # calculate the distance

        # execute the movement


def main():
    data = np.array([-3, 4, -1, 2])
    assert data.shape == (4,)

    whaleOptimizationAlgorithm(data, 2)


if __name__ == "__main__":
    main()
