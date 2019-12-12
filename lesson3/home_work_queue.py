class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

q = Queue()

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print('isEmpty ', q.isEmpty())
print('Size ', q.size())

print('Queue ', q)

q.dequeue()
print('Size ', q.size())

print(q)