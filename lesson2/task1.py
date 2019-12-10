print('hi')

class Vehicle:

    def __init__(self, weight, brand, max_speed):
        self._weight = weight
        self._brand = brand
        self._max_speed = max_speed

    def wher_is_car(self):
        print(f'{_brand} Stay')

class Car(Vehicle):

    def __init__(self, driver_name, weight, brand, max_speed):
        self._driver_name = driver_name
        super().__init__(weight, brand, max_speed)

    def wher_is_car(self):
        print(f'{self._brand} Not Stay')

class Truck(Vehicle):

    def __init__(self, truck_id, weight, brand, max_speed):
        self._truck_id = truck_id
        super().__init__(weight, brand, max_speed)

    def wher_is_car(self):
        print(f'{self._brand} Far')


car = Car('me', 1500, 'bmw', 200)
truck = Truck('C100', 4000, 'Mercedes' , 100)

print(car._brand)
car.wher_is_car()

print(truck._brand)
truck.wher_is_car()