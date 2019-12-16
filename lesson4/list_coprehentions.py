import time

start = time.time()
a = []

for i in range(100):
    if i % 2 == 0:
        a.append(i)

end = time.time() - start

# =

start_compor = time.time()

dict = {
    1:2,
    3:4,
    5:6,
}


odds = {i:j for i, j in dict.items()}

print(odds)

end_compor = time.time() - start_compor

if end_compor < end:
    print('Comperhention faster')


