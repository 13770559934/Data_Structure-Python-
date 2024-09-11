from Stack import Stack;
from BinaryTree2 import BinaryTree2;
import operator;

def buildParseTree(astring):
    alist = astring.split();
    pstack = Stack();
    eTree = BinaryTree2('');
    pstack.push(eTree);
    current_tree = eTree;

    for i in alist:
        if i == '(':
            current_tree.insertleft('');
            pstack.push(current_tree);
            current_tree = current_tree.getleftchild();

        elif i == ')':
            current_tree = pstack.pop();

        elif i not in ['+', '-', '*', '/']:
            current_tree.setroot(int(i));
            current_tree = pstack.pop();

        elif i in ['+','-','*','/']:
            current_tree.setroot(i);
            current_tree.insertright('');
            pstack.push(current_tree);
            current_tree = current_tree.getrightchild();

        else:
            raise ValueError;

    return eTree;


def evaluate(parseTree):
    opers = {'+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv};

    leftc = parseTree.getrightchild();
    rightc = parseTree.getleftchild();

    if leftc and rightc:
        fn = opers[parseTree.getroot()];
        return fn(evaluate(leftc), evaluate(rightc));

    else:
        return parseTree.getroot();

