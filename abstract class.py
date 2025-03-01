from abc import ABC, abstractmethod

class Vehicle:
     @abstractmethod
     def export(self):
         pass

     def import1(self):
         print("this is import")
        


class Car(Vehicle):

    def export (self):
        print("this is export")


car=Car()

car.export()

car.import1()
