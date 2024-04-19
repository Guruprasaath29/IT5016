# Define a function named calculate_average that takes a variable number of arguments
def calculate_average(*args):
    # Calculate the total marks by summing all the arguments
    total_marks = sum(args)
    # Count the number of subjects (arguments)
    num_subjects = len(args)
    # Calculate the average by dividing the total marks by the number of subjects
    average = total_marks / num_subjects
    # Print the average
    print("The average is:", average)
    
    # Check if the average is greater than or equal to 50
    if average >= 50:
        # If the average is greater than or equal to 50, print "pass"
        print("Pass")
    else:
        # If the average is less than 50, print "fail"
        print("Fail")

# Call the calculate_average function with marks as arguments
calculate_average(20, 40, 30)
