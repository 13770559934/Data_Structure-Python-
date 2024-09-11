from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None;

    def isEmpty(self):
        return self.head == None;

    def add(self, item):
        node_obj = Node(item)
        node_obj.next = self.head;
        self.head = node_obj;

    def size(self):
        current = self.head;
        size = 0;
        while current.next != None :
            size += 1;
            current = current.next;

        return size;

    def search (self, item):
        current = self.head;
        found = False;
        while not found and current.data != None:
            if current.data == item:
                found = True;
            else:
                current = current.next;
        return found;

    def remove (self, item):
        current = self.head;
        previous = None;
        found = False;
        while not found :
            if current.data == item:
                found = True;
            else:
                previous = current;
                current = current.next;

        if previous == None:
            self.head = current.getNext();

        else:
            previous.setNext(current.getNext());
    