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
    
    # Initialize the first week
    last_added = low_risk[0] # Last_added index so we can keep track and remove later if the upcoming week high risk is rewarding
    total += last_added

    return total
low_risk = [10, 1, 10, 10]
high_risk = [5, 50, 5, 1]
print(optimal_plan(low_risk, high_risk))  # Expected output should be 70