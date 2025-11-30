import unittest
from unittest.mock import patch

import numpy as np

from Strategies.BubbleNetAttackingMethod import BubbleNetAttackingMethod


class TestBubbleNetAttack(unittest.TestCase):

    def setUp(self):
        """
        Prepare the strategy instance before every test.
        """
        # 'b' is the constant defining the shape of the logarithmic spiral
        self.b_constant = 1.0
        self.strategy = BubbleNetAttackingMethod().set_b(self.b_constant)

        # Simulate the behavior of setXstar() from the parent class
        # We define a target (Best Whale) at position [10, 10]
        self.strategy.Xstar = np.array([10.0, 10.0])

    @patch("src.Strategies.BubbleNetAttackingMethod.np.random.uniform")
    def test_move_spiral_simple(self, mock_random):
        """
        Test the spiral move with l = 0.
        This is the 'Base Case' because e^0 = 1 and cos(0) = 1.

        Formula: X(t+1) = D' * e^(bl) * cos(2πl) + X*
        If l=0:  X(t+1) = D' * 1 * 1 + X* = D' + X*
        """
        # -------------------------------------------------------
        # 1. ARRANGE
        # -------------------------------------------------------
        # Force random number 'l' to be 0.0
        mock_random.return_value = 0.0

        # Current whale position
        current_whale = np.array([2.0, 2.0])

        # -------------------------------------------------------
        # 2. ACT
        # -------------------------------------------------------
        new_position = self.strategy.move(current_whale)

        # -------------------------------------------------------
        # 3. ASSERT (Manual Math Verification)
        # -------------------------------------------------------
        # X* = [10, 10]
        # X  = [2, 2]
        # b  = 1.0
        # l  = 0.0
        #
        # Step 1: Calculate Distance to Prey (D')
        # D' = |X* - X|
        # D' = |10 - 2| = 8
        #
        # Step 2: Calculate Spiral Terms
        # Exp Term: e^(b*l) = e^0 = 1
        # Cos Term: cos(2*pi*l) = cos(0) = 1
        #
        # Step 3: Final Position
        # Pos = (D' * Exp * Cos) + X*
        # Pos = (8 * 1 * 1) + 10 = 18

        expected_position = np.array([18.0, 18.0])

        np.testing.assert_array_almost_equal(
            new_position,
            expected_position,
            err_msg="Spiral calculation failed for simple case (l=0)",
        )

    @patch("src.Strategies.BubbleNetAttackingMethod.np.random.uniform")
    def test_move_spiral_complex(self, mock_random):
        """
        Test the spiral move with l = -1.
        Formula: X(t+1) = D' * e^(bl) * cos(2πl) + X*
        """
        # -------------------------------------------------------
        # 1. ARRANGE
        # -------------------------------------------------------
        # Force 'l' to be -1.0.
        # Note: cos(-2π) is 1.0, which simplifies the trig part
        # but keeps the exponential part active.
        mock_random.return_value = -1.0

        # Current whale position at Origin
        current_whale = np.array([0.0, 0.0])

        # -------------------------------------------------------
        # 2. ACT
        # -------------------------------------------------------
        new_position = self.strategy.move(current_whale)

        # -------------------------------------------------------
        # 3. ASSERT (Manual Math Verification)
        # -------------------------------------------------------
        # X* = [10, 10]
        # X  = [0, 0]
        # b  = 1.0
        # l  = -1.0
        #
        # Step 1: Calculate Distance (D')
        # D' = |10 - 0| = 10
        #
        # Step 2: Calculate Spiral Terms
        # Exp Term: e^(1 * -1) = e^-1 ≈ 0.367879
        # Cos Term: cos(2 * pi * -1) = 1.0
        #
        # Step 3: Final Position
        # Pos = (10 * 0.367879 * 1.0) + 10
        # Pos = 3.67879 + 10 = 13.67879

        expected_val = (10.0 * np.exp(-1.0)) + 10.0
        expected_position = np.array([expected_val, expected_val])

        np.testing.assert_array_almost_equal(
            new_position,
            expected_position,
            decimal=5,
            err_msg="Spiral calculation failed for complex case (l=-1)",
        )


if __name__ == "__main__":
    unittest.main()
