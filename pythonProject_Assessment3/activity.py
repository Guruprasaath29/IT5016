m=str(input("Enter your message:"))
count=0
for l in m:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        count += 1

print(" vowels:", count)