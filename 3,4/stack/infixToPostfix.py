from stack_first_as_bottom import Stack;

def infixToPostfix(equation):

    #首先，弄个dict表示优先级。

    prec = {};
    prec['('] = 1;
    prec['+'] = 2;
    prec['-'] = 2;
    prec['*'] = 3;
    prec['/'] = 3;

    opstack = Stack(); #先写一个stack
    postfixList = []; # output list
    equation_list = equation.split(); # split the input

    for token in equation_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token);
        
        elif token == '(':
            opstack.push(token);

        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfixList.append(topToken);
                topToken = opstack.pop();

        else:
            while (not opstack.isEmpty()) and (prec[token] < prec[opstack.peek()]):
                postfixList.append(opstack.pop());
            opstack.push(token);

        #last step: pop everything is the stack into the outpust list.
    while not opstack.isEmpty():
        postfixList.append(opstack.pop());

    return ''.join(postfixList);
            
print(infixToPostfix('A + ( B + C ) * D'));