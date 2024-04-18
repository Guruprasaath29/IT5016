class Cars:
    # initialise the function
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def car(self):
        return (" The name of the car is " + self.name)

    def mil(self):
        Kilometer  = self.mileage * 10
        return (Kilometer)


i = Cars("Toyota Mark X", "150km/hr", 15.50)

print(i.car())
print(i.mil())
