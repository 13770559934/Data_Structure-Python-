from stack_first_as_bottom import stack;
import matches as mt

def parchecker (symbolstring):
    tempstack = stack();
    for i in symbolstring:
        if i in '([{':
            tempstack.push(i);
        elif i in ')]}':
            if mt.matches2(tempstack.peek(), i):
                tempstack.pop();

    return tempstack.isEmpty()


print (parchecker('((()))'))
print (parchecker('((())'))
print (parchecker('[(())]'))
