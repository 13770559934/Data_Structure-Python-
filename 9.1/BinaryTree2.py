class BinaryTree2:
    def __init__(self,rootobj):
        self.key = rootobj;
        self.leftchild = None;
        self.rightchild = None;

    def insertleft(self,newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree2(newNode);

        else:
            t = BinaryTree2(newNode);
            t.leftchild = self.leftchild;
            self.leftchild = t;

    def insertright(self, newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree2(newNode);

        else:
            t = BinaryTree2(newNode);
            t.rightchild = self.rightchild;
            self.leftchild = t;

    def getrightchild(self):
        return self.rightchild;

    def getleftchild(self):
        return self.leftchild;

    def getroot(self):
        return self.key;

    def setroot(self,obj):
        self.key = obj;

    def preorder(self):
        print(self.key);

        if self.leftchild != None:
            self.leftchild.preorder();
        if self.rightchild != None:
            self.rightchild.preorder();


r = BinaryTree2("a");

r.insertleft("b");
r.insertleft("d");
r.insertright("c");

r.getrightchild().setroot("hello");

r.getleftchild().insertright("d");