import unittest
from optimal_stock_buyer import when_to_buy

class TestWhenToBuy(unittest.TestCase):

    def test_all_decreasing(self):
        print("Testing all decreasing prices...")
        prices = [5, 4, 3, 2, 1]
        result = when_to_buy(prices)
        self.assertEqual(result, [])
        print("Test passed.") if result == [] else print("Test failed.")

    def test_all_increasing(self):
        print("Testing all increasing prices...")
        prices = [1, 2, 3, 4, 5]
        expected_result = [(0, 1), (1, 2), (2, 3), (3, 4)]
        result = when_to_buy(prices)
        self.assertEqual(result, expected_result)
        print("Test passed.") if result == expected_result else print("Test failed.")

    def test_random_prices(self):
        print("Testing random prices...")
        prices = [5, 3, 2, 5, 6, 1, 4]
        expected_result = [(2, 3), (3, 4), (5, 6)]
        result = when_to_buy(prices)
        self.assertEqual(result, expected_result)
        print("Test passed.") if result == expected_result else print("Test failed.")

    def test_alternating_prices(self):
        print("Testing alternating prices...")
        prices = [5, 1, 5, 1, 5]
        expected_result = [(1, 2), (3, 4)]
        result = when_to_buy(prices)
        self.assertEqual(result, expected_result)
        print("Test passed.") if result == expected_result else print("Test failed.")

    def test_minimum_length(self):
        print("Testing minimum length...")
        prices = [5, 6]
        expected_result = [(0, 1)]
        result = when_to_buy(prices)
        self.assertEqual(result, expected_result)
        print("Test passed.") if result == expected_result else print("Test failed.")

    def test_maximum_length(self):
        print("Testing maximum length...")
        prices = [5, 6, 4, 8, 2, 10, 1]
        expected_result = [(0, 1), (2, 3), (4, 5)]
        result = when_to_buy(prices)
        self.assertEqual(result, expected_result)
        print("Test passed.") if result == expected_result else print("Test failed.")

    def test_invalid_length_too_short(self):
        print("Testing invalid length too short...")
        prices = [5]
        with self.assertRaises(ValueError):
            when_to_buy(prices)
        print("Test passed.") 

    def test_invalid_length_too_long(self):
        print("Testing invalid length too long...")
        prices = [5, 6, 4, 8, 2, 10, 1, 7]
        with self.assertRaises(ValueError):
            when_to_buy(prices)
        print("Test passed.") 

if __name__ == '__main__':
    unittest.main()