# Define a function named sum that takes a parameter lengtharray
def sum(lengtharray):
    # Initialize an empty list named result to store the numbers
    result = []
    # Initialize a variable named total to store the sum of the numbers
    total = 0
    
    # Iterate 'lengtharray' times to get 'lengtharray' numbers from the user
    for i in range(lengtharray):
        # Prompt the user to input a number and convert it to an integer
        n = int(input("Enter a number: "))
        # Append the number to the result list
        result.append(n)
    
    # Print the list of numbers entered by the user
    print("Numbers entered:", result)
    
    # Calculate the total sum of the numbers in the result list
    for i in result:
        total += i
    
    # Print the total sum of the numbers
    prin
