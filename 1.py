class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Transport is moving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"

my_car = Transport("Toyota", 120)

print(my_car)

my_car.move()

print(f"Марка машины: {my_car.brand}")