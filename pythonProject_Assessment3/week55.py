# Define a function named percentage that takes a variable number of arguments
def percentage(*args):
    # Calculate the total sum of the arguments
    total = sum(args)
    # Calculate the average by dividing the total sum by the number of arguments
    avg = total / len(args)
    # Return the average
    return avg

# Example usage of the percentage function
# Calculate the average of the numbers 56, 61, and 73
avg = percentage(56, 61, 73)
# Print the calculated average
print('Average =', avg)
