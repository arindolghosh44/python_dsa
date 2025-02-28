"""class Car:
    def __init__(self, modelName="Unknown", create="Unknown", name="Unknown"):
        self.modelName = modelName
        self.create = create
        self.name = name

# Creating instances with different argument combinations
honda = Car("fhfhhf", "8", "honda")
bike = Car()  # Uses default values
thor = Car("ffgrrrrrrrrrrrrrrr", "8888")  # Uses default for 'name'

# Printing attribute of honda object
print(honda.create)  # Output: 8
print(honda.name)"""



#Another way using args with particular value

class Car:
    def __init__(self, *args):
        if len(args) == 3:  # If three arguments are provided
            self.modelName, self.create, self.name = args
        elif len(args) == 2:  # If two arguments are provided
            self.modelName, self.create = args
            self.name = "Unknown"  # Default value for name
        elif len(args) == 1:  # If one argument is provided
            self.modelName = args[0]
            self.create = "Unknown"
            self.name = "Unknown"
        else:  # If no arguments are provided
            self.modelName = "Unknown"
            self.create = "Unknown"
            self.name = "Unknown"

# Creating instances
honda = Car("fhfhhf", "8", "honda")  
bike = Car()  
thor = Car("ffgrrrrrrrrrrrrrrr", "8888")  

# Output
print(honda.create)  # Output: 8
print(bike.modelName)  # Output: Unknown
print(thor.name)  # Output: Unknown
print(bike. __dict__)
