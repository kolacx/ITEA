class MyList:

    def __init__(self, size):
        self._my_list = [0] * size
        self._size = size

    def clear(self):
        self._my_list = []
        return self._my_list

    def pop(self):
        del self._my_list[-1]
        return self._my_list

    def append(self, value):
        return self._my_list + [value]

    def __str__(self):
        return str(self._my_list)

a = MyList(10)

print(a)

# a.clear()
a.pop()
a.append('123')
print(a)