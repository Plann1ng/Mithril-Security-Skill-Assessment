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
if __name__ == '__main__':
    unittest.main()
