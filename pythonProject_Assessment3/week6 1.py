# Define a class named Fruit
class Fruit:
    # Define the constructor method to initialize name and color attributes
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Define a method named func to print a message indicating the name of the fruit
    def func(self):
        print("Fruit is " + self.name)

# Create an instance of the Fruit class with name "Banana" and color "Yellow"
f1 = Fruit("Banana", "Yellow")

# Call the func method of the Fruit instance
# This will print "Fruit is Banana"
print(f1.func())
