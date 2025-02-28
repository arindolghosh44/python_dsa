"""class Parent:
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        print("This is parent class method")

class Child(Parent):
    def __init__(self, a=2, b=2, c=2):
        super().__init__(a, b, c)  # Call Parent constructor to set attributes

    def add(self):
        print("This is child class method")

# Creating objects
child1 = Child()

print(child1.a)  # Now this will work! Output: 2"""




class Parent:
    a=1
    b=1
    c=1
    def add(self):
        print("this is parent class")


class child(Parent):
    a=2
    b=2
    c=2
    def add(self):
        print("this is child class")


parent=Parent()

child1=child()

parent.add()
child1.add()


print(child1.a)
