def matches(i, j):
    """
This function is used to check if ( matches ), [ matches ], { matches }.
    """
    opens = '([{';
    closes = ')]}';

    return opens.index(i) == closes.index(j);
    

def matches2(i, j):
    if i == '(' and j == ')':
        return True
    elif i == '[' and j == ']':
        return True
    elif i == '{' and j == '}':
        return True
    else:
        return False;
