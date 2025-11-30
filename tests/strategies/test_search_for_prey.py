import unittest
from unittest.mock import patch

import numpy as np

# Adjust import to match your structure
from src.Strategies.SearchForPrey import SearchForPrey


class TestSearchForPrey(unittest.TestCase):

    def setUp(self):
        """
        Prepare the strategy instance.
        """
        self.A_val = 0.5
        self.strategy = SearchForPrey(self.A_val)

        # Define a dummy population (simulating 'data' in your loop)
        # Whale 0: [0, 0]
        # Whale 1: [10, 10] (We will pretend this is the Randomly Selected one)
        # Whale 2: [20, 20] (We will pretend this is the Global Best/Xstar)
        self.population = [
            np.array([0.0, 0.0]),
            np.array([10.0, 10.0]),
            np.array([20.0, 20.0]),
        ]

    @patch("src.Strategies.EncirclingPrey.throwACoinBetween0to1")
    def test_C_calculation(self, mock_coin):
        """
        Test C() - Inherited from EncirclingPrey.
        """
        mock_coin.return_value = 0.3
        expected_C = 2 * 0.3
        actual_C = self.strategy.C()
        self.assertEqual(actual_C, expected_C)

    @patch("src.Strategies.EncirclingPrey.throwACoinBetween0to1")
    def test_move_towards_random_neighbor(self, mock_coin):
        """
        Test the move logic specifically simulating the 'Search' behavior.

        In the main loop:
        1. A random whale is picked (we simulate this manually).
        2. setXstar() is called with that random whale.
        3. move() is called.
        """
        # -------------------------------------------------------
        # 1. ARRANGE (Simulate the Main Loop Logic)
        # -------------------------------------------------------

        # A. Simulate picking a random index (e.g., index 1)
        random_index = 1
        random_whale_sample = self.population[random_index]  # [10.0, 10.0]

        # B. Set this random whale as the target (Just like in your loop)
        self.strategy.setXstar(random_whale_sample)

        # C. Mock the coin for C calculation
        # We want C = 1.0, so coin = 0.5
        mock_coin.return_value = 0.5

        # D. Define current whale position
        current_whale = np.array([2.0, 2.0])

        # -------------------------------------------------------
        # 2. ACT
        # -------------------------------------------------------
        new_position = self.strategy.move(current_whale)

        # -------------------------------------------------------
        # 3. ASSERT (Manual Math Verification)
        # -------------------------------------------------------
        # Target (X*) = [10, 10] (The random whale)
        # Current (X) = [2, 2]
        # A = 0.5
        # C = 1.0
        #
        # Step 1: Distance D = |C * X* - X|
        # D = |1.0 * [10,10] - [2,2]| = [8, 8]
        #
        # Step 2: New Pos = X* - A * D
        # Pos = [10,10] - 0.5 * [8,8]
        # Pos = [10,10] - [4,4] = [6, 6]

        expected_position = np.array([6.0, 6.0])

        np.testing.assert_array_almost_equal(
            new_position,
            expected_position,
            err_msg="SearchForPrey did not move correctly towards the assigned random whale.",
        )


if __name__ == "__main__":
    unittest.main()
