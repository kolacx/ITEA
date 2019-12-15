class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0,item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

q = Queue()

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print('is_empty ', q.is_empty())
print('Size ', q.size())

print('Queue ', q)

q.dequeue()
print('Size ', q.size())

print(q)