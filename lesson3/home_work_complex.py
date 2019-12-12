class MyComplex:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'({self.real}+{self.imag}j)'

    def __add__(comp1, comp2):
        return MyComplex(comp1.real + comp2.real, comp1.imag + comp2.imag)


a = MyComplex(1,2)
b = MyComplex(2,3)

z = a + b 

print(z)