from abc import ABC, abstractmethod

class Vehicle(ABC): ## abstract class

    @property
    @abstractmethod
    def bike(self): ## abstarct method
        pass


class car(Vehicle):

    @property
    def bike(self):
        return 4



car=car()

print(car.bike)
