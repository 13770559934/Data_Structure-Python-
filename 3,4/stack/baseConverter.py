from unicodedata import digit
from stack_first_as_bottom import Stack;

def baseConverter(base,num):
    digit = '0123456789ABCDEF';

    temp_Stack = Stack();

    output = '';

    while num > 0:
        temp_num = num % base;
        temp_Stack.push(temp_num);
        num = num // base;

    while not temp_Stack.isEmpty():
        output += digit[temp_Stack.pop()]

    return output;


print(baseConverter(2,25));