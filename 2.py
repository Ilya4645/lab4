class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving.")


    def __str__(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, brand, seats, speed):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Beep beep!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __str__(self):
        return f"{super().__str__()}, Seats: {self.seats}"

class Bike(Vehicle):
    def __init__(self, brand, bike_type, speed=0):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")
        
    def __str__(self):
        return f"{super().__str__()}, Type: {self.type}"

my_car = Car("Toyota", 5, 60)
print(my_car)
my_car.move()
my_car.honk()

v = Vehicle('ddd', 60)
print(v)
v.move()

print("-" * 20)

my_bike = Bike("Trek", "mountain", 20)
print(my_bike)
my_bike.move()