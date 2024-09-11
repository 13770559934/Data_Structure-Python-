class Queue:
    def __init__(self):
        self.contant = [];

    def enqueue(self, item):
        self.contant.insert(0, item);

    def dequeue(self):
        return self.contant.pop()

    def isEmpty(self):
        return self.contant == []

    def size(self):
        return len(self.contant);
