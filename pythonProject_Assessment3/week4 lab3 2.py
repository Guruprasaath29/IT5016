# Define a function named calculator that takes two parameters, a and b
def calculator(a, b):
    # Calculate the addition of a and b
    addition = a + b
    # Calculate the subtraction of b from a
    subtraction = a - b
    # Return both addition and subtraction results
    return addition, subtraction

# Call the calculator function with arguments 5 and 5
# Assign the returned values (addition and subtraction results) to sum_add and sum_sub respectively
sum_add, sum_sub = calculator(5, 5)

# Print the result of addition
print("Addition:", sum_add)
# Print the result of subtraction
print("Subtraction:", sum_sub)
