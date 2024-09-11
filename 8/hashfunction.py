def hash(astring, tablesize):
    sum = 0;
    for pos in astring:
        sum += ord(pos);

    return sum % tablesize;

print(hash("hello", 11));