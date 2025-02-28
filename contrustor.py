"""
class Car:
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

"""


#without using 
class Car:
    def __init__(self, modelName, create, name):
        self.modelName = modelName
        self.create = create
        self.name = name

# Creating instances with different argument combinations
honda = Car("fhfhhf", "8jjjj", "honda")
bike = Car("fhfhhf", "8", "honda")  # Uses default values
thor = Car("ffgrrrrrrrrrrrrrrr", "8888","fhfh")  # Uses default for 'name'

# Printing attribute of honda object
print(honda.name)  # Output: 8
