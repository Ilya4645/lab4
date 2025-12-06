class Transport:
    def move(self):
        print("Транспорт движется.")

class Car(Transport):
    def move(self):
        print("Автомобиль едет по дороге.")

class Bike(Transport):
    def move(self):
        print("Велосипед едет по тропинке.")

objects = [Car(), Bike(), Transport()]

for obj in objects:
    obj.move()
