class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


s = Stack()

s.push('a')
s.push('b')

print(s.isEmpty())
print(s.size())
print(s.peek())