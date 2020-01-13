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
        self._my_list[len(self._my_list):] = [value]
        return self._my_list

    def insert(self, position, value):
        self._my_list[position : position] = [value]
        return self._my_list

    def remove(self, value):
        for k, v in enumerate(self._my_list):
            if v == value:
                del self._my_list[k]
                break


    def __str__(self):
        return str(self._my_list)

