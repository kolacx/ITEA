class MyComplex:
    def __init__(self, real, imag=0.0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return f'({self._real}+{self._imag}j)'

    def __add__(comp1, comp2):
        return MyComplex(comp1._real + comp2._real, comp1._imag + comp2._imag)

    def __mul__(comp1, comp2):
        return MyComplex(comp1._real * comp2._real, comp1._imag * comp2._imag)

    def __sub__ (comp1, comp2):
        return MyComplex(comp1._real - comp2._real, comp1._imag - comp2._imag)

    def __truediv__ (comp1, comp2):
        return MyComplex(comp1._real / comp2._real, comp1._imag / comp2._imag)


a = MyComplex(1,2)
b = MyComplex(2,3)

res1 = a + b 
res2 = a * b 
res3 = a - b 
res4 = a / b 

print('__add__ ', res1)
print('__mul__ ', res2)
print('__sub__ ', res3)
print('__truediv__ ', res4)