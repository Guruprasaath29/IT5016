import random

class Membership:
    status = "Active"  # Class attribute for membership status

    def __init__(self):
        # Initialize instance attributes
        self.student_id = ''
        self.stud_lastname = ''
        self.stud_program = ''
        self.mem_id = ''
        self.status = Membership.status  # Assigning class attribute to instance attribute

    # Method to input student data
    def stud_data(self):
        self.student_id = input("Enter your Whitecliffe student Id: ")
        self.stud_lastname = input("Enter your last name: ")
        self.stud_program = input("Enter the name of your programme (diploma/degree): ")

    # Method to generate membership ID
    def generate_mem_id(self):
        registered_stud = ['S1', 'S2', 'S3', 'S4', 'S5']
        if self.student_id in registered_stud:
            g_mem_id = random.randint(1, 10)
            return g_mem_id

    # Method to display membership information
    def display(self):
        print("Membership ID:", self.mem_id)
        print("Student ID:", self.student_id)
        print("Last Name:", self.stud_lastname)
        print("Program:", self.stud_program)
        print("Status:", self.status)

    # Method to withdraw a student
    def withdrawal(self, ln):
        if self.stud_lastname == ln:
            self.status = "Withdrawn"

# List to store registered students
registration = []

# Input number of students to register
num = int(input("How many students are you registering today? "))

# Registering students
for i in range(num):
    # Create an instance of Membership class
    k = Membership()
    # Input student data
    k.stud_data()
    # Generate membership ID
    k.mem_id = k.generate_mem_id()
    # Display membership information
    k.display()
    # Withdraw student with last name 'Guru'
    k.withdrawal("Guru")
    # Add student to registration list
    registration.append(k)

# Withdraw a specific student
name = input("Enter the name of the student withdrawing: ")
for i in range(num):
    registration[i].withdrawal(name)

# Display membership information of withdrawn students
for i in range(num):
    registration[i].display()

# Count various statistics
active = 0
withdrawn = 0
diploma = 0
degree = 0
for i in range(num):
    if registration[i].status == "Active":
        active += 1
    if registration[i].status == "Withdrawn":
        withdrawn += 1
    if registration[i].stud_program.lower() == "diploma":
        diploma += 1
    if registration[i].stud_program.lower() == "degree":
        degree += 1

# Print statistics
print("The number of active members:", active)
print("The number of withdrawn students:", withdrawn)
print("The number of diploma students:", diploma)
print("The number of degree students:", degree)
