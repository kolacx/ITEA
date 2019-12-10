class Dots:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def __mul__ (dot1, dot2):
        return Dots(dot1._x * dot2._x, dot1._y * dot2._y, dot1._z * dot2._z)

    def __add__ (dot1, dot2):
        return Dots(dot1._x + dot2._x, dot1._y + dot2._y, dot1._z + dot2._z)

    def __sub__ (dot1, dot2):
        return Dots(dot1._x - dot2._x, dot1._y - dot2._y, dot1._z - dot2._z)

    def __div__ (dot1, dot2):
        return Dots(dot1._x / dot2._x, dot1._y / dot2._y, dot1._z / dot2._z)

    # def __pos__ (dit1, dot2):
    #     return Dots()

dot1 = Dots(1,2,3)

dot2 = Dots(1,2,3)

dot3 = dot1 * dot2

print(dot3.get_x())
print(dot3.get_y())
print(dot3.get_z())

dot1 += dot2