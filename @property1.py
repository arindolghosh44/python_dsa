"""class Person:
    def __init__(self,name="unknown"):
        self._name=name

    @property
    def getName(self):
        return self._name



person=Person("alice")

print(person.getName)"""

##Using @property with a Setter

class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

# Usage
p = Person("Alice")
p.name = "Bob"  # Works fine
print(p.name)  # Output: Bob
# p.name = 123  # Raises ValueError


class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

# Usage
p = Person("Alice")
del p.name  # Output: Deleting name...



class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.1416 * (self._radius ** 2)

# Usage
c = Circle(5)
print(c.area)  # Output: 78.54

