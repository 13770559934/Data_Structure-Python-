def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                temp = alist[j];
                alist[j] = alist[j+1];
                alist[j+1] = temp;


def bubbleSort2(alist):
    exchange = True;
    passnum = len(alist) - 1;
    while passnum > 0 and exchange:
        exchange = False;
        for j in range(passnum):
            if alist[j] > alist[j+1]:
                temp = alist[j];
                alist[j] = alist[j+1];
                alist[j+1] = temp;
                exchange = True;
        passnum -= 1;


alist = [90,97,22,18,12,9,8,4,1];

bubbleSort2(alist);

print(alist);