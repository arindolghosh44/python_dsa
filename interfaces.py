from abc import ABC, abstractmethod

# Defining an interface
class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Implementing the interface
class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

# Implementing another class using the same interface
class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

# Using the classes
car = Car()
car.start()  # Output: Car started
car.stop()   # Output: Car stopped

bike = Bike()
bike.start()  # Output: Bike started
bike.stop()   # Output: Bike stopped
