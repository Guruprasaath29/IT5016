# Initialize an empty list to store city names
city = []

# Prompt the user to enter city names five times and add them to the list
for i in range(5):
    city_name = input("Enter a city name: ")
    city.append(city_name)

# Print the list of cities
print("Cities:", city)

# Print the length of the list
print("Length of the array:", len(city))

# Add a new city ("Hong") to the end of the list
city.append("Hong")
print("Updated Cities:", city)

# Remove the first city from the list
city.pop(0)
print("Cities after removing the first element:", city)

# Reverse the order of the cities in the list
city.reverse()
print("Reversed array:", city)
