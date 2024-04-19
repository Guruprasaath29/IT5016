# Prompt the user to enter the student ID
student_id = input("Enter the student ID: ")
# Prompt the user to enter the first name of the student
student_fn = input("Enter the first name of the student: ")
# Prompt the user to enter the last name of the student
student_ln = input("Enter the last name of the student: ")

# Define a message
message = "I am a newbie In Whitecliffe college !"
# Split the message into words
words = message.split()

# Print the words in the message
print("Words in the message:", words)

# Iterate through each word in the message
for i in words:
    # Check if the word is "Whitecliffe" or "college"
    if i == "Whitecliffe" or i == "college":
        # If the word is "Whitecliffe" or "college", print it
        print(i)
