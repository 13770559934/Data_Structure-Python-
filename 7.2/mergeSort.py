from heapq import merge


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2;
        leftside = alist[:mid];
        rightside = alist[mid:];

        mergeSort(leftside);
        mergeSort(rightside);

        i = j = k = 0;

        while i < len(rightside) and j < len(leftside):
            if rightside[i] < leftside[j]:
                alist[k] = rightside[i];
                i += 1;

            else:
                alist[k] = leftside[j];
                j += 1;

            k += 1;


        while i < len(rightside):
            alist[k] = rightside[i];
            i += 1;
            k += 1;

        while j < len(leftside):
            alist[k] = leftside[j];
            j += 1;
            k += 1;


def mergesort2(alist):

    if len(alist) <= 1:
        return alist;

    middle = len(alist) // 2;
    right = mergesort2(alist[middle:]);
    left = mergesort2(alist[:middle]);

    merged = [];
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0));

        else:
            merged.append(right.pop(0));


    merged.extend(right if right else left);
    return merged;

alist = [90,97,22,18,12,9,8,4,1];

print(mergesort2(alist));