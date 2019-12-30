# функции высшего порятка

list_of_names = ['kolya', 'vasya', 'petya', 'nikolay']

def makeing_upper(string):
    return string.upper()

#1
results = []
for name in list_of_names:
    results.append(makeing_upper(name))

print(results)
#2

result2 = [makeing_upper(name) for name in list_of_names]
print(result2)

#3
print(list(map(makeing_upper, list_of_names)))

# lambda

print(list(map(lambda x, y: (x.upper(), y.upper()), list_of_names, list_of_names)))

mr = map(lambda x, y: (x.upper(), y.upper()), list_of_names, list_of_names)

print(list(mr))


#filter

def func(extra_value, **kwargs):
    for k, v in kwargs.items():
        if v == extra_value:
            kwargs.pop(k)
            break

    return kwargs


# ==

extra_value = 'token'
kwargs = {
    'sum': 12,
    'id': 135134,
    'comment': 'user_coment',
    'token': 'asd'
}

d1 = dict(filter(lambda kv: kv[1] != extra_value, kwargs.items()))    
d2 = func(extra_value, **kwargs)
print(d1)
print(d2)