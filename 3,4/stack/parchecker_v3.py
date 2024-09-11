from stack_first_as_bottom import Stack;
import matches;

def parchecker(symbolstring):
    tempstack = Stack();
    i = 0;
    checker = True;
    while i < len(symbolstring) and checker:
        if symbolstring[i] in '{[(':
            tempstack.push(symbolstring[i]);
        elif symbolstring[i] in ')]}':
            if matches.matches(tempstack.peek(), symbolstring[i]):
                tempstack.pop();
            else:
                checker = False;
        i += 1;

    if not tempstack.isEmpty():
        checker = False;

    return checker;

print (parchecker('((()))'))
print (parchecker('((())'))
print (parchecker('[(())]'))
