from turtle import position


def gapinsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i];
        position = i;

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position - gap];
            position = position - gap;

        alist[position] = currentvalue;



def shellsort(alist):
    sublistcount = len(alist) // 2;
    while sublistcount > 0:
        for startpoint in range(sublistcount):
            gapinsertionSort(alist, startpoint, sublistcount);

        print("After increment of size", 
        sublistcount,
        "The list is", alist
        )

        sublistcount //= 2;

alist = [90,97,22,18,12,9,8,4,1];

shellsort(alist);

print(alist);