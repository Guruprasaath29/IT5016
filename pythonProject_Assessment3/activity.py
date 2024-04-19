# Prompt the user to enter a message
m = str(input("Enter your message:"))

# Initialize a variable to store the count of vowels
count = 0

# Loop through each character in the message
for l in m:
    # Check if the character is a vowel (a, e, i, o, or u)
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        # If the character is a vowel, increment the count
        count += 1

# Print the count of vowels in the message
print("vowels:", count)
