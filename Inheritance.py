class Car:
    def __init__(self, modelName="Unknown", create="Unknown", name="Unknown"):
        self.modelName = modelName
        self.create = create
        self.name = name


class superCar(Car):
    pass


# Creating instances with different argument combinations
honda = superCar("fhfhhf", "8", "honda")
bike = superCar()  # Uses default values
thor = Car("ffgrrrrrrrrrrrrrrr", "8888")  # Uses default for 'name'



print(honda.name)
