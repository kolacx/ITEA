import random

class Randomizer:

    def __init__(self, steps):
        self._steps = steps
        self._current_step = 0
        self._value = 0

    def __iter__(self):
        return self

    def __next__(self):
        
        if self._current_step <= self._steps:
            self._value += random.random()
            self._current_step += 1

        else:
            raise StopIteration()
            
        return self._value

obj = Randomizer(1000)

for i in obj:
    print(i)