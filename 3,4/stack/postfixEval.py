import re
from stack_first_as_bottom import Stack;

def postfixEval(postfix_equation):
    #make a stack
    opstack = Stack();
    #make a equation list to iter
    input_equation = postfix_equation.split()

    for token in input_equation:
        if token in '0123456789':
            opstack.push(int(token));
        
        else:
            opnum2 = opstack.pop();
            opnum1 = opstack.pop();
            result = domath(token, opnum1, opnum2);
            opstack.push(result);

    return opstack.pop();


def domath(op, op1, op2):
    if op == '*':
        return op1 * op2;

    elif op == '/':
        return op1 / op2;

    elif op == '+':
        return op1 + op2;

    elif op == '-':
        return op1 - op2;


print(postfixEval('3 7 * 2 8 * +'))