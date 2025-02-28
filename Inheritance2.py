class Car:
    def __init__(self, modelName="Unknown", voice="Unknown", make="Unknown", years="Unknown", price="Unknown"):
        self.modelName = modelName
        self.voice = voice
        self.make = make
        self.years = years
        self.price = int(price) if str(price).isdigit() else 0  # Ensure price is an integer
    
    def price_inc(self):
        self.price = int(self.price * 1.15)

class SuperCar(Car):
    def thririr(self, value, rate):  # Added 'self'
        print(value)
        print(rate)

    def __init__(self,modelName="Unknown", voice="Unknown", make="Unknown", years="Unknown", price="Unknown",cc="Unknown"):
        """self.modelName = modelName
        self.voice = voice
        self.make = make
        self.years = years
        self.price = int(price) if str(price).isdigit() else 0  # Ensure price is an integer """ # no need to write whole code
        super(). __init__(modelName="Unknown", voice="Unknown", make="Unknown", years="Unknown", price="Unknown")
        self.cc=cc


# Creating objects
honda = SuperCar("Lamborghini", "Dorami", "New One", "2014", 12345,"cc")
print(honda.cc)
honda.thririr(242, 67.56)

# Corrected object initialization
tata = Car("Thor", "Sound", "Tata", "2022", 12345555)
htor = Car("Piii", "Dggd")

# Checking price increment
print("Before price increase:", honda.price)
honda.price_inc()
print("After price increase:", honda.price)

# Displaying car details
print("Tata Model:", tata.modelName)
print("Tata Price:", tata.price)
print("Htor Model:", htor.modelName)
print("Htor Voice:", htor.voice)
