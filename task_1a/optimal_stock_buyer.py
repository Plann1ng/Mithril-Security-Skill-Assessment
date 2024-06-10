def when_to_buy(prices):
    # Ensuring that the list is in the proper range
    if not (2 <= len(prices) < 8):
        raise ValueError("Number of prices must be between 2 and 7 for this function to work properly.")
    print(f"Calculating transactions for prices: {prices}")

    # Resulting string will be stored here
    result = []

    # Lenght of the given list should be value (n)
    n = len(prices)

    # Start iteration from day 2
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            result.append((i - 1, i))
            print(f"Transaction found: Buy on day {i}, Sell on day {i + 1}")
    return result

prices = [5, 3, 2, 5, 6, 1, 4]
transactions = when_to_buy(prices)
