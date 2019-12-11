import time


def decorator(num_of_iterations):
    time_start = time.time()
    def decorator_in(func):
    
        def wrapper(number):
            print('Wrapper start')

            result = []

            for i in range(num_of_iterations):
                result.append(func(number))

            print(f'Wrapt result is {result}')
            print('Wrapper end')


            time_miss = time.time() - time_start
            print(func.__name__, time_miss)

            return result

        return wrapper

    return decorator_in


@decorator(4)
def my_func(number):
    sum_number = 0 
    for i in range(number):
        sum_number += i

    return sum_number

my_func(3)

