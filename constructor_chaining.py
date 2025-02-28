class Parent:
    def __init__(self,name):
        self.name=name
        print(f"parent contrustructor calling {self.name}")


class child1(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print(f"child1 contrustructor calling {self.age}")

class child2(child1):
    def __init__(self,name,age,rate):
        super().__init__(name,age)
        self.rate=rate
        print(f"child2 contrustructor calling {self.rate}")



child2_object=child2("john",21,234)
