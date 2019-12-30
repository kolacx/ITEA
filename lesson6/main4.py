# generator

def counter(start, end):

    while start <= end:
        yield start
        start += 1
        print('gen func')


def randomizer(steps):
    import random

    current_step = 0
    value = 0

    while current_step <= steps:
        value += random.random()
        current_step += 1
        yield value


for i in randomizer(10):
    print(i)