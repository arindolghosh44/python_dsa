from abc import ABC, abstractmethod

class Engine(ABC):  # Interface 1
    @abstractmethod
    def start_engine(self):
        pass

    @property
    @abstractmethod
    def end_wheels(self):
        pass

class Wheel(ABC):  # Interface 2
    @abstractmethod
    def engine_count(self):
        pass

class Car(Engine, Wheel):  # Implementing both interfaces
    @property
    def end_wheels(self):
        return 6  # Example: 6-wheeled vehicle

    def engine_count(self):
        return 90  # Example: 90 HP engine

    def start_engine(self):
        print("Start the engine:")

# Creating an instance of Car
car = Car()

print(car.end_wheels)  # Access property without ()
print(car.engine_count())  # Call method with ()
car.start_engine()  # Output: Start the engine:
