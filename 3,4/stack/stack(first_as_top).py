class stack:
    def __init__(self):
        self.items = []

    def push(self,i):
        self.items.insert(0,i);

    def pop(self):
        self.items.pop(0);

    def peek(self):
        return self.items[0];

    def isEmpty(self):
        return self.items == [];

    def size(self):
        return len(self.items);


s = stack();

for i in range(100):
    s.push(i);

print(type(s));

print(s.isEmpty());

print(s.peek());

s.pop();

print(s.peek());
