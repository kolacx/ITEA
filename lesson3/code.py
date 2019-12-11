def a(a_arg):
    print(a_arg)

    def b(b_arg):
        print(b_arg)

        def c(c_arg):
            print(c_arg)
            print('The end of function tree')


        return c


    return b

a(10)(20)(30)
print(a(10)(20)(30))


print('-' * 10)

# Decorator

def random_generator():
    import random
    print(random.randint(0,100))


def func1(func):

    print('Hello i am func1')
    print('Func start')
    func()
    print('Func end')


func1(random_generator)

#Decorator2
print('-' * 10)


def random_generator2(range_start, renge_end):
    import random
    return random.randint(range_start, renge_end)

def decorator(func):

    def wrapper(range_start, renge_end):
        print('start wrap')
        result = func(range_start, renge_end)
        print(f'Wrapt result is {result}')
        print('end wrap')

        return result

    return wrapper #обьект функции

@decorator
def random_generator3(range_start, renge_end):
    import random
    return random.randint(range_start, renge_end)


# result = decorator(random_generator2)(100, 200) 
# print(result)

print('-' * 10)

result = random_generator3(100, 200)

print(result)