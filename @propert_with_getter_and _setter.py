## getter and setter
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        """Calculated property for area (No setter since it’s derived)"""
        return self._width * self._height

# Usage
r = Rectangle(5, 10)
print(r.area)  # Output: 50
r.width = 7  # Changing width
print(r.area)  # Output: 70
