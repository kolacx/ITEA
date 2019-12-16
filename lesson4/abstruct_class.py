from abc import ABC, abstractmethod


class Vehicle(ABC):

    attr = 1

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def beep(self):
        # pass
        print('Default')


# Vehicle()

class Car(Vehicle):

    def move(self):
        print('Moving')

    def beep(self):
        # print('Beep')
        super().beep()


print(dir(Vehicle))
Car().move()
Car().beep()

#  Ошибка будет тогда когда будет обращение к данному методу
class MyABC:

    def my_method(self):
        raise NoImplementedError


class MyClass(MyABC)
    pass