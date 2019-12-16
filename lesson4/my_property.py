
class Dot:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, value):
        self._x = value

    def get_x(self, value):
        return self._x

    def set_y(self, value):
        self._y = value

    def get_y(self, value):
        return self._y

    x = property(get_x, set_x)

    # @property
    # def x(self):
    #     return self._x

    # @x.setter
    # def x(self, value):
    #     if value < 0:
    #         print('value mast be positive')
    #         self._x = 0
    #         return None
    #     self._x = value

obj = Dot(1, 2)

print(obj.x)

obj.x = -2

print(obj.x)