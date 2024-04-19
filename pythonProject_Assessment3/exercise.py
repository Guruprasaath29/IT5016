# Initialize empty lists to store student names and ages
student_name = []
student_age = []

# Prompt the user to input student names and ages for 7 students
for i in range(7):
    # Input student name
    name = input("Enter student name: ")
    # Input student age
    age = int(input("Enter student age: "))
    
    # Append the name and age to their respective lists
    student_name.append(name)
    student_age.append(age)

# Print the list of student names
print("Student Names:", student_name)
# Print the list of student ages
print("Student Ages:", student_age)
