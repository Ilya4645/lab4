class Transport:
    def __init__(self, brand, seats, speed):
        self.brand = brand
        self.seats = seats
        self.speed = speed

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

    def __eq__(self, other):
        if isinstance(other, Transport):
            return self.speed == other.speed
        return False

    def move(self):
        print(f"{self.brand} is moving.")

class Car(Transport):
    def __init__(self, brand, seats, speed):
        super().__init__(brand, seats, speed)

    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

    def __len__(self):
        return self.speed

    def honk(self):
        print("Beep beep!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        raise TypeError("Можно складывать только объекты класса Car")

class Bike(Transport):
    def __init__(self, brand, seats, speed):
        super().__init__(brand, seats, speed)

    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")


g_t = Transport('Bus', 20, 120)
car1 = Car('Toyota', 5, 160)
car2 = Car('Jeep', 5, 140)
car3 = Car('Haval', 5, 160)
bike1 = Bike('BMX', 1, 40)
bike2 = Bike('NoName', 1, 30)

print(g_t)
print(car1)
print(car2)
print(car3)
print(bike1)
print(bike2)

g_t.move()
car1.move()
car1.honk()
car2.move()
car3.move()
bike1.move()
bike2.move()
print(len(car1))

print(f"car1 == car2 (по скорости)? {car1 == car3}")
total_speed = car1 + car2
print(f"Суммарная скорость car1 и car2: {total_speed}")

try:
    result = car1 + bike1
    print(f"Результат car1 + bike1: {result}")
except TypeError as e:
    print(f"Произойдет ошибка TypeError: {e}")

