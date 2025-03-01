from abc import ABC

class Animal(ABC): #abstract class

    a=1
    b=1666
    c=1
    def eat(self):
        print("animake is eating")



class sub(Animal): # extends the abstract class 
    pass


cub=sub()

print(cub.a,cub.b)

cub.eat()
