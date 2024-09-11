import time;

def aragramSolution2(s1 , s2):
    start = time.time();
    list2 = list(s2.lower());
    pos1 = 0;
    stillOk = True;
    while stillOk and pos1 < len(s1):
        pos2 = 0;
        found = False;
        while not found and pos2 < len(list2):
            if s1[pos1] == list2[pos2]:
                found = True;
                list2[pos2] = None;
            else:
                pos2 += 1;
        if found:
            list2[pos2] = None;
        else:
            stillOk = False;
        pos1 += 1;
        end = time.time();
    return (stillOk, end - start);

print("%s, %10.7f"
    %aragramSolution2('python','typhon'));
        
