import unittest
from unittest.mock import patch

import numpy as np

# Update this import path to match your actual project structure
from src.Strategies.EncirclingPrey import EncirclingPrey


class TestEncirclingPrey(unittest.TestCase):

    def setUp(self):
        """
        Prepare the strategy instance before every test.
        """
        self.A_val = 0.5
        self.strategy = EncirclingPrey(self.A_val)

        # Simulate the behavior of setXstar() from the parent class
        # We define a target (Best Whale) at position [10, 10]
        self.strategy.Xstar = np.array([10.0, 10.0])

    @patch("src.Strategies.EncirclingPrey.throwACoinBetween0to1")
    def test_C_calculation(self, mock_coin):
        """
        Test the C() method specifically.
        Formula: C = 2 * r
        """
        # Force random coin to return 0.3
        mock_coin.return_value = 0.3

        expected_C = 2 * 0.3  # = 0.6
        actual_C = self.strategy.C()

        self.assertEqual(actual_C, expected_C)

    @patch("src.Strategies.EncirclingPrey.throwACoinBetween0to1")
    def test_calculate_distance(self, mock_coin):
        """
        Test the intermediate distance calculation.
        Formula: D = |C * X* - X|
        """
        # 1. Setup
        mock_coin.return_value = 0.5  # So C = 2 * 0.5 = 1.0
        current_whale = np.array([2.0, 2.0])

        # 2. Execute
        # Distance = |1.0 * [10,10] - [2,2]| = |[8,8]| = [8, 8]
        distance = self.strategy.calculateDistance(current_whale)

        # 3. Assert
        expected_distance = np.array([8.0, 8.0])
        np.testing.assert_array_almost_equal(distance, expected_distance)

    @patch("src.Strategies.EncirclingPrey.throwACoinBetween0to1")
    def test_move_full_logic(self, mock_coin):
        """
        Test the final move() method.
        Formula: NewPos = X* - A * D
        """
        # -------------------------------------------------------
        # 1. ARRANGE
        # -------------------------------------------------------
        # We want C to be 1.0 to make math easy, so coin must be 0.5
        mock_coin.return_value = 0.5

        # Current whale position
        current_whale = np.array([2.0, 2.0])

        # -------------------------------------------------------
        # 2. ACT
        # -------------------------------------------------------
        new_position = self.strategy.move(current_whale)

        # -------------------------------------------------------
        # 3. ASSERT (Manual Math Verification)
        # -------------------------------------------------------
        # A = 0.5 (set in setUp)
        # X* = [10, 10]
        # C = 1.0
        #
        # Step 1: Distance (D)
        # D = |C * X* - X|
        # D = |1.0 * 10 - 2| = 8
        #
        # Step 2: New Position
        # Pos = X* - A * D
        # Pos = 10 - (0.5 * 8)
        # Pos = 10 - 4 = 6

        expected_position = np.array([6.0, 6.0])

        np.testing.assert_array_almost_equal(
            new_position,
            expected_position,
            err_msg="The final move position calculation is incorrect.",
        )


if __name__ == "__main__":
    unittest.main()
