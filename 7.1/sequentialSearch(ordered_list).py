def orderedsequentialSearch(alist, item):
    stop = False;
    found = False;
    pos = 0;

    while not stop and not found:
        if alist[pos] == item:
            found = True;
        elif alist[pos] > item:
            stop = True;

        else:
            pos += 1;

    return found

testlist = [0,1,3,4,5,9,10,12,20]

print(orderedsequentialSearch(testlist, 12))