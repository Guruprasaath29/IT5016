# input the user to enter a score within the range of 0 to 100
score = int(input("Enter the score (0-100): "))

# Validate the score to ensure it falls within the specified range
while score < 0 or score > 100:
    score = int(input("Invalid score. Enter the score (0-100): "))

# Initialize an empty string to store the grade
grade = ""

# Assign a grade based on the score
while True:
    if score >= 80:
        grade = "A"
        break
    elif score >= 60:
        grade = "B"
        break
    elif score >= 50:
        grade = "C"
        break
    else:
        grade = "Fail"
        break

# Print the grade
print("Grade:", grade)
