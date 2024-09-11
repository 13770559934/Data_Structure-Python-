from os import curdir
from Node import Node;

class OrderedList:
    def __init__(self):
        self.head = None;

    def add(self, item):
        previous = None;
        current = self.head;
        stop = False;
        while not stop and current != None:
            if current.getData() > item:
                stop = True;
            else:
                previous = current;
                current = current.getNext();

        temp = Node(item);
        if previous == None:
            temp.setNext(self.head);
            self.head = temp;
        else:
            temp.setNext(current);
            previous.setNext(temp);
    
    def isEmpty(self):
        return self.head == None;

    def size(self):
        current = self.head;
        size = 0;
        while current.next != None :
            size += 1;
            current = current.next;

        return size;

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

    def search(self, item):
        current = self.head;
        found = False;
        stop = False;
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True;
            elif current.getData() > item:
                stop = True;
            else:
                current = current.getNext();

        return found;