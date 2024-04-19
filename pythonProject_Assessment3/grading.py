# Prompt the user to enter the score for the first subject
m1 = int(input("Enter the score for the first subject: "))
# Prompt the user to enter the score for the second subject
m2 = int(input("Enter the score for the second subject: "))

# Calculate the total score
total = m1 + m2
# Calculate the average score
avg = total / 2

# Check if the average score is greater than or equal to 50
if avg >= 50:
    # If the average score is greater than or equal to 50, print "pass"
    print("Pass")
else:
    # If the average score is less than 50, print "fail"
    print("Fail")
