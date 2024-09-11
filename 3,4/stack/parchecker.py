from stack_first_as_bottom import Stack;

def parchecker (symbolstring):
    tempstack = Stack();
    for i in symbolstring:
        if i == '(':
            tempstack.push(i);
        elif i == ')':
            tempstack.pop();

    return tempstack.isEmpty()


print (parchecker('((()))'))
print (parchecker('((())'))
print ()
