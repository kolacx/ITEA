# generator

def counter(start, end):

    while start <= end:
        yield start
        start += 1


c = counter(0, 100)

print(c)
for i in c:
    print(i)