def partition(alist, first, last):
    pivotvalue = alist[first];

    leftmark = first + 1;
    rightmark = last;

    done = False;

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1;

        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1;

        if rightmark < leftmark:
            done = True;

        else:
            temp = alist[leftmark];
            alist[leftmark] = alist[rightmark];
            alist[rightmark] = temp;

    temp = alist[rightmark];
    alist[rightmark] = alist[first];
    alist[first] = temp;

    return rightmark;


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last);

        quickSortHelper(alist, first, splitpoint - 1);
        quickSortHelper(alist, splitpoint + 1, last);


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1);



alist = [90,97,1,100,1000,2,45];

quickSort(alist);

print(alist);