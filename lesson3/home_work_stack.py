class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def size(self):
        return len(self._items)


s = Stack()

s.push('a')
s.push('b')

print('is_empty ', s.is_empty())
print('Size ', s.size())
print('Pop ', s.pop())