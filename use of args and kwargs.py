#Correct! Without a Class, We Do Not Need self
#args is used when you don't know how many arguments will be passed.
def gdddg(*args):
    sum1=sum(args)#sum predefined methods
    print(sum1)

gdddg(1,2,3,4)
gdddg(4,5)


#**kwargs allows us to pass named (keyword) arguments.
#It collects arguments into a dictionary.



def print_info(**kwargs):
    for key,value in kwargs.items():
        #print("{key}:{value}")
         print(f"{key}:{value}")



print_info(name="john",age=222,thor="iyiy")



def mix_function(*args,**kwargs):
    print("for args:",args)
    print("for kwargs:",kwargs)

mix_function(1,2,3,name="john",age=222,thor="iyiy")


"""
class Car:
    def __init__(self, *args, **kwargs):
        self.model = kwargs.get("model", "Unknown")
        self.price = kwargs.get("price", 0)
    
    def display(self):
        print(f"Car Model: {self.model}, Price: {self.price}")

car1 = Car(model="Tesla", price=50000)
car1.display()"""


class Car:
    def __init__(self, *args):
        if len(args) >= 2:
            self.model = args[0]  # First argument as model
            self.price = args[1]  # Second argument as price
        else:
            self.model = "Unknown"
            self.price = 0

    def display(self):
        print(f"Car Model: {self.model}, Price: {self.price}")

# Creating objects with different arguments
car1 = Car("Tesla", 50000)
car2 = Car("BMW")  # Only model, price will be default 0
car3 = Car()  # No arguments, both values default

car1.display()  # Output: Car Model: Tesla, Price: 50000
car2.display()  # Output: Car Model: BMW, Price: 0
car3.display()  # Output: Car Model: Unknown, Price: 0




class Student:
    def __init__(self, name, *subjects):
        self.name = name
        self.subjects = subjects  # `subjects` will be a tuple

    def display(self):
        print(f"Student: {self.name}, Subjects: {', '.join(self.subjects)}")

# Creating an object with multiple subjects
student1 = Student("Alice", "Math", "Science", "English")
student1.display()  # Output: Student: Alice, Subjects: Math, Science, English

