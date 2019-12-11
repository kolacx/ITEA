def random_generator(range_start, renge_end):
    import random
    return random.randint(range_start, renge_end)


def decorator(func):

    def wrapper(range_start, renge_end):
        result = []

        for i in range(100):
            result.append(func(range_start, renge_end))

        
        return result


    return wrapper


