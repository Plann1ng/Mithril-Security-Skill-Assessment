import unittest
from stock_predictions import optimal_plan

class TestOptimalPlan(unittest.TestCase):

    def test_example_case(self):
        low_risk = [10, 1, 10, 10]
        high_risk = [5, 50, 5, 1]
        self.assertEqual(optimal_plan(low_risk, high_risk), 70)
        print("Example case test passed.")
    
    def test_no_weeks(self):
        low_risk = []
        high_risk = []
        self.assertEqual(optimal_plan(low_risk, high_risk), 0)
        print("No weeks test passed.")

    def test_all_low_risk(self):
        low_risk = [10, 10, 10, 10]
        high_risk = [5, 5, 5, 5]
        self.assertEqual(optimal_plan(low_risk, high_risk), 40)
        print("All low risk test passed.")

    def test_all_high_risk(self):
        low_risk = [1, 1, 1, 1]
        high_risk = [10, 10, 10, 10]
        self.assertEqual(optimal_plan(low_risk, high_risk), 10)  # High risk always chosen
        print("All high risk test passed.")

    def test_mixed_risk(self):
        low_risk = [5, 5, 5, 5]
        high_risk = [10, 10, 1, 1]
        self.assertEqual(optimal_plan(low_risk, high_risk), 20)
        print("Mixed risk test passed.")

    def test_equal_value_all_risk(self):
        low_risk = [5, 5, 5, 5, 5]
        high_risk = [5, 5, 5, 5, 5]
        self.assertEqual(optimal_plan(low_risk, high_risk), 25)
        print("Equal value all risk test passed.")

    def test_single_element(self):
        low_risk = [10]
        high_risk = [20]
        self.assertEqual(optimal_plan(low_risk, high_risk), 10)
        print("Single element test passed.")

    def test_alternating_values(self):
        low_risk = [5, 5, 5, 5, 5]
        high_risk = [10, 1, 10, 1, 10]
        self.assertEqual(optimal_plan(low_risk, high_risk), 25)
        print("Alternating values test passed.")

    def test_increasing_sequence(self):
        low_risk = [1, 2, 3, 4, 5]
        high_risk = [6, 7, 8, 9, 10]
        self.assertEqual(optimal_plan(low_risk, high_risk), 10)
        print("Increasing sequence test passed.")

    def test_decreasing_sequence(self):
        low_risk = [5, 4, 3, 2, 1]
        high_risk = [10, 9, 8, 7, 6]
        self.assertEqual(optimal_plan(low_risk, high_risk), 6)
        print("Decreasing sequence test passed.")
if __name__ == '__main__':
    unittest.main()
