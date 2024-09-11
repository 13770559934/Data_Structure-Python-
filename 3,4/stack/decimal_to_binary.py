from stack_first_as_bottom import Stack;

def decimal_to_binary(num):
    stack = Stack();

    while num > 0:
        rem = num % 2;
        num = num // 2
        stack.push(rem)

    binary = '';
    while not stack.isEmpty():
        binary += str(stack.pop());

    return binary;


print(decimal_to_binary(35));
