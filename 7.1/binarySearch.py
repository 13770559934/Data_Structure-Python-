def binarySearch(alist, item):
    first = 0;
    last = len(alist) - 1;
    found = False;

    while first <= last and not found:
        midpoint = (first + last) // 2;
        if alist[midpoint] == item:
            found = True;

        elif alist[midpoint] < item:
            first = midpoint + 1;

        elif alist[midpoint] > item:
            last = midpoint - 1;

    return found;

print (binarySearch([1,3,4,10,11,19,20,25,90],90));