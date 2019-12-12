class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


s = Stack()

s.push('a')
s.push('b')

print('isEmpty ', s.isEmpty())
print('Size ', s.size())
print('Pop ', s.pop())