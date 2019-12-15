import time


def decorator(num_of_iterations):
    time_start = time.time()
    def decorator_in(func):
    
        def wrapper(*args):
            print('Wrapper start')

            result = []

            for i in range(num_of_iterations):
                result.append(func(*args))

            print(f'Wrapt result is {result}')
            print('Wrapper end')


            time_miss = time.time() - time_start
            print(func.__name__, time_miss)

            return result

        return wrapper

    return decorator_in


@decorator(4)
def my_func(*args):
    
    result = []
    for item in args:
        for later in item:
            result.append(later)

    return result


word1 = 'hello'
word2 = 'world'

result = my_func(word1, word2)

print(result)

