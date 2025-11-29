import numpy as np
import plotly.express as px


def create_data(distribution, how_many, dimensional):
    if distribution == 'uniform':
        return np.random.uniform(size=(how_many, dimensional))
    elif distribution == 'normal':
        return np.random.normal(size=(how_many, dimensional))


# we consider that our problem is 1-dimensional
def F(x):
    return x**2


def calculateFitnessForAllData(data):
    x_dimensional_of_the_data = data
    return F(x_dimensional_of_the_data)


def findTheXStarIndex(fitnessVector):
    return np.argmin(fitnessVector)


def whaleOptimizationAlgorithm(data, max_iteration):
    # make a copy of original data
    data = data.copy()
    for iteration in range(max_iteration):
        fitnessVector = calculateFitnessForAllData(data)

        x_star_index = findTheXStarIndex(fitnessVector)

        x_star_value = data[x_star_index]

        print(x_star_value)

        # choose the movement type

        # calculate the distance

        # execute the movement






def main():
    data = np.array([-3, 4, -1, 2])
    assert data.shape == (4,)

    whaleOptimizationAlgorithm(data, 2)


if __name__ == '__main__':
    main()