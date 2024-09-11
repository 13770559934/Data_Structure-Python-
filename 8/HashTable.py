class HashTable:
    def _init_(self,size):
        self.size = size;
        self.slots = [None] * self.size;
        self.data = [None] * self.size;

    def hashfunctioin(self, key):
        return key%self.size;

    def rehash(self,oldhash):
        return (oldhash + 1) % self.size;

    def put(self, key, data):
        hashvalue = self.hashfunction(key);

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key;
            self.data[hashvalue] = data;

        elif self.slots[hashvalue] == key:
            self.data[hashvalue];

        else:
            nexthash = self.rehash(hashvalue);
            while self.slots[nexthash] != None and self.slots[nexthash] != key:
                nexthash = self.rehash(nexthash);

            if self.slots [nexthash] == None:
                self.slots[nexthash] = key;
                self.data[nexthash] = data;

            else:
                self.data[nexthash] = data;

    def get(self, key):
        startslot = self.hashfunctioin(key);

        data = None;
        stop = False;
        found = False;
        position = startslot;

        while not stop and not found and self.slots[position] != None:
            if self.slots[position] == key:
                found = True;
                data = self.data[position];

            elif position == startslot:
                stop = True;

            else:
                position = self.rehash(position);

        return data;

    def __getitem__ (self, key):
        return self.get(key);
    
    def __setitem__ (self, key, data):
        return self.put(key,data);