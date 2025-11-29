import numpy as np

from src.Strategies.EncirclingPrey import EncirclingPrey
from src.utils.throw_coin import throwACoinBetween0to1


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
            return EncirclingPrey(A_parameter)
        else:
            return EncirclingPrey(A_parameter)
            # return SearchForPrey()
    else:
        return EncirclingPrey(A_parameter)
        # return BubbleNetAttackingMethod()


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

        x_star_sample = data[x_star_index]

        for data_sample_index, data_sample in enumerate(data):
            probability = throwACoinBetween0to1()

            # a parameter is a number that is reducing from 2 to 0 during iterations
            a_parameter = a(iteration_number, max_iteration)

            # what exactly is the A parameter?
            A_parameter = A(a_parameter)

            movementObject = chooseMovementStrategyRandomly(probability, A_parameter)

            new_data_sample = movementObject.setXstar(x_star_sample).move(data_sample)

            data[data_sample_index] = new_data_sample

        print(data)


def main():
    data = np.array([[-3], [4], [-1], [2]])
    assert data.shape == (4, 1)

    whaleOptimizationAlgorithm(data, 10)


if __name__ == "__main__":
    main()
