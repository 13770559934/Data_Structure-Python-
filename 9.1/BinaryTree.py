class BinaryTree:
    def __init__(self,r, right = None, left = None):
        self.tree = [r, left, right];

    def insertleft(self, newbranch):
        t = self.tree.pop(1);

        if t == None:
            temp = BinaryTree(newbranch);
            self.tree.insert(1, temp);

        else:
            temp = BinaryTree(newbranch, left = t);
            self.tree.insert(1, temp);

    def insertright(self, newbranch):
        t = self.tree.pop(2);

        if len(t) > 1:
            self.tree.insert(2, [newbranch, [], t]);

        else:
            self.tree.insert(2, [newbranch , [], []]);

    def getroot (self):
        return self.tree[0];

    def setroot (self, newval):
        self.tree[0] = newval;

    def getleft (self):
        return self.tree[1];

    def getright (self):
        return self.tree[2];


r = BinaryTree(3);
r.insertleft(4);
r.insertleft(5);

print(r.getroot());
print(r.getleft().getleft().getroot());
print(r.getright());