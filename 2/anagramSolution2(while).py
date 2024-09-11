import time;

def aragramSolution2 (s1, s2):
    start = time.time()
    list1 = list(s1.lower());
    list2 = list(s2.lower());

    list1.sort()
    list2.sort()
    # sort() is a list method

    pos = 0;
    matches = True;
    while pos < len(list1) and matches:
        if list1[pos] != list2[pos]:
            matches = False;
        else:
            pos += 1;

    end = time.time()
    return (matches, end - start);

print("%s, %10.7f"
    %aragramSolution2('Python','typhon'));
