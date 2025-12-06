class Car:
    def __init__(self, brand, seats, speed):
        self.brand = brand
        self.seats = seats
        self.speed = speed

    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        raise TypeError("Можно складывать только объекты класса Car")

if __name__ == "__main__":
    car1 = Car('Toyota', 4, 180)
    car2 = Car('Subaru', 5, 200)

    print(f"Количество мест в car1: {len(car1)}")
    print(f"Количество мест в car2: {len(car2)}")

    print(f"car1 == car2 (по скорости)? {car1 == car2}")

    total_speed = car1 + car2
    print(f"Суммарная скорость car1 и car2: {total_speed}")

    try:
        t_s = car1 + 100
    except TypeError as e:
        print(f"Ошибка при попытке сложения: {e}")