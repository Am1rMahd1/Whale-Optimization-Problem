import numpy as np
import plotly.express as px


def create_data(distribution, how_many, dimensional):
    if distribution == 'uniform':
        return np.random.uniform(size=(how_many, dimensional))
    elif distribution == 'normal':
        return np.random.normal(size=(how_many, dimensional))


# we consider that our problem is 2-dimensional
def F(x, y):
    return x**2 + y**2

def whaleOptimizationAlgorithm(data, max_iteration):
    for iteration in range(max_iteration):
        pass

    # iteration = ?

    # p = np.random.rand




def main():
    # data = create_data('normal', 10, 2)
    # assert data.shape == (10, 2)
    data = np.array([-3, 4, -1, 2])
    assert data.shape == (4,)


if __name__ == '__main__':
    main()