class MyDict:

    def __init__(self, k, v):
        self._my_dict = dict(k=v)

    def __str__(self):
        return str(self._my_dict)        

a = MyDict('k'='v')

print(a)