

def sum_func(*args):
    print(*args)
    print(args)


a = [1, 2, 3, 4]

b = {}

sum_func(*a)
# = Same
sum_func(1, 2, 3, 4)

def sum_func_2(*args):
    result = 0
    for i in args:
        print(i)
        result += i

    return result

print(sum_func_2(*a))