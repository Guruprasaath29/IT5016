# Prompt the user to enter the score for M1
M1 = float(input("Enter M1: "))
# Prompt the user to enter the score for M2
M2 = float(input("Enter M2: "))
# Prompt the user to enter the score for M3
M3 = float(input("Enter M3: "))
# Prompt the user to enter the score for M4
M4 = float(input("Enter M4: "))

# Calculate the average grade
Grade = (M1 + M2 + M3 + M4) / 4

# Check if the average grade is less than 50
if Grade < 50:
    # If the average grade is less than 50, print "fail"
    print("Fail")
else:
    # If the average grade is 50 or more, print "pass"
    print("Pass")
