print('hi lesson 2 ООП')

class Vehicle:

    # vehicle_type = 'Car' #Переменная Класа

    def __init__(self, num_of_doors ,num_of_wheels, brand ):
        self._num_of_doors = num_of_doors #переменные обьекта
        self._num_of_wheels = num_of_wheels
        self._brand = brand

    def get_barnd(self):
        return self._brand

    def get_car_info(self):
        return dict(
            num_of_doors = self._num_of_wheels,
            num_of_wheels = self._num_of_wheels
            )

    def move(self):
        print('Moving')


class Car(Vehicle):

    def __init__(self, num_of_doors ,num_of_wheels, brand, max_weight ):
        self.max_weight = max_weight
        super().__init__(num_of_doors ,num_of_wheels, brand)
        self._engine = 'V-8'

    def transport_smth(self, weight, thing):
        print(f'Transporting {thing}. Max weight {weight}')

    def _chang_oil(self): 
        print('asd')

    def set_engine(self, value):
        if type(value) != str:
            raise Exception('wrong type')
        self._engine = value

    def __str__(self):
        return self._brand




# print(Vehicle.vehicle_type)
# car = Vehicle(4,4,'BMW')
# car.move()

# car.num_of_wheels = 10

# print(car.num_of_wheels)
# print(car.brand)
# print(car.num_of_doors)
# print(car.vehicle_type)

# car.vehicle_type = "Truck"
# print(car.vehicle_type)

# print(Vehicle.vehicle_type)

# сar.new_variable = 100
# print(car.new_variable)

car1 = Car(4,4,"Mercedes", 400)
car1.move()
car1.transport_smth(200, 'Animals')

car1.set_engine('v-12')
print(car1._engine) # tak nelzya

# print(car1.get_car_info())

# print(dir(car1))

# print(car1.__dict__['_num_of_wheels'])

# print(dir(Car))

# print(Car.__dict__)

print(car1) 