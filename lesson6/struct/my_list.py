class MyList:

    def __init__(self, *args):
        self._my_list = [*args]
        self._steps = len(args)
        self._current_step = 0

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

    def __iter__(self):
        return self

    def __next__(self):
        
        if self._current_step <= self._steps - 1:
            res = self._my_list[self._current_step]
            self._current_step += 1
            return res

        else:
            raise StopIteration()

    def __add__(l1, l2):

        new_list = MyList()

        for i in l1:
            new_list.append(i)

        for i in l2:
            new_list.append(i)

        return new_list

    def __str__(self):
        return str(self._my_list)

ll1 = MyList(1, 2, 3)
ll2 = MyList(4, 5, 6)

print(ll1+ll2)