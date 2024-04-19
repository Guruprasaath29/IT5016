# Prompt the user to input the student ID
Student_id = input("Enter student ID: ")
# Validate the input: continue prompting until the input consists only of digits
while Student_id.isdigit() == False:
    Student_id = input("Invalid input. Please enter student ID: ")

# Prompt the user to input the student's first name
First_name = input("Enter student first name: ")
# Validate the input: continue prompting until the input consists only of alphabetic characters
while First_name.isalpha() == False:
    First_name = input("Invalid input. Please enter student first name: ")

# Prompt the user to input the student's last name
Last_name = input("Enter last name: ")
# Validate the input: continue prompting until the input consists only of alphabetic characters
while Last_name.isalpha() == False:
    Last_name = input("Invalid input. Please enter last name: ")
