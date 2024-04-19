# Define a function named average_student that takes keyword arguments (**kwargs)
def average_student(**kwargs):
    # Initialize a variable sum to store the sum of scores
    sum = 0
    # Iterate over the values of the keyword arguments (scores)
    for i in kwargs.values():
        # Calculate the sum of scores
        sum += i
    # Calculate the average by dividing the sum by the number of scores
    avg = sum / len(kwargs)
    # Return both the sum and average
    return sum, avg

# Call the average_student function with keyword arguments representing scores for different subjects
k = average_student(IT5014=60, IT7809=80, IT6798=50, IT5048=70)
# Print the sum and average returned by the function
print("Sum & average:", k)
