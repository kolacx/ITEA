def decorator(func):

    def wrapper(start, end):
        print('start')
        res = func(start, end)
        print(res)

        return res

    return wrapper


@decorator
def asd(start, end):
    import random
    return random.randint(start, end)



a = asd(100, 200)

print(a)

