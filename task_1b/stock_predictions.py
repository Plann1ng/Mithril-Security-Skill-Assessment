def optimal_plan(low_risk, high_risk):
    # Lists must be the same lenght
    n = len(low_risk)

    # Optimal output
    total = 0

    # If the list is empty
    if (n == 0):
        return 0

    # If the list lenght do not match
    elif (len(low_risk) != len(high_risk)):
        raise ValueError("High-risk and Low-risk lenght must be the same!")
    
    # First week always low risk since there is no possible n-1
    last_added = low_risk[0] # Last_added index so we can keep track and remove later if the upcoming week high risk is rewarding
    total += last_added

    # Starting from the second week
    for i in range(1, n):
    # If current week high risk is better than low risk, remove the previously added number from total
        if high_risk[i] > low_risk[i]:
            total -= last_added
            last_added = high_risk[i]
            total += last_added
    # If low risk is better, then just add
        else:
            last_added = low_risk[i]
            total += last_added
    return total

low_risk = [10, 1, 10, 10]
high_risk = [5, 50, 5, 1]
print(optimal_plan(low_risk, high_risk))  # Expected output should be 70