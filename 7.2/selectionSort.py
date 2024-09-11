def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        positionofMax = 0;
        for j in range(1,i+1): #这边注意了！！！
            if alist[j] > alist[positionofMax]:
                positionofMax = j;

        temp = alist[positionofMax]
        alist[positionofMax] = alist[j];
        alist[j] = temp;



alist = [90,97,22,18,12,9,8,4,1];

selectionSort(alist);

print(alist);