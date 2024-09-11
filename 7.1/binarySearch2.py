def binarySearch(alist, item):
    midpoint = len(alist) // 2;
    if len(alist) == 0:
        return False;
    
    elif alist[midpoint] == item:
        return True;

    elif alist[midpoint] < item:
        return binarySearch(alist[midpoint+1:], item);

    elif alist[midpoint] > item:
        return binarySearch(alist[:midpoint-1],item);


print(binarySearch([1,3,4,10,11,19,20,25,90],3));