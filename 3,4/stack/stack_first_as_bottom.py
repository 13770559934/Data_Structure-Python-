class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [];

    def push(self,i):
        self.items.append(i);

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

"""
s = stack();

for i in range(100):
    s.push(i);

print(type(s));

print(s.isEmpty());

print(s.peek());

s.pop();

print(s.peek());
"""
