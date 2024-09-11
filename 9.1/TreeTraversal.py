from BinaryTree2 import BinaryTree2;

def preorder(tree):
    if tree != None:
        print(tree.getroot());
        preorder(tree.getleftchild());
        preorder(tree.getrightchild());

def inorder(tree):
    if tree != None:
        inorder(tree.getleftchild());
        print(tree.getroot());
        inorder(tree.getrightchild());

def postorder(tree):
    if tree != None:
        postorder(tree.getleftchild());
        postorder(tree.getrightchild());
        print(tree.getroot()); 