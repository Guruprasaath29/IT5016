# Define a function named fruit_name that takes keyword arguments (**kwargs)
def fruit_name(**kwargs):
    # Iterate over the keys of the keyword arguments (fruit names)
    for i in kwargs.keys():
        # Print each fruit name
        print(i)

# Call the fruit_name function with keyword arguments representing fruit names and quantities
fruit_name(mangoes=1, oranges=2, apples=3)
