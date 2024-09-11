import time;

def aragramSolution2(s1,s2):
    start = time.time()
    list1 = list(s1.lower());
    list2 = list(s2.lower());

    list1.sort()
    list2.sort()

    if len(list1) != len(list2):
        return "Please enter two stings which have the same length."

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            end = time.time();
            return (False, end - start);

    end = time.time();
    return(True, end - start);


print("%s, %10.7f"
    %aragramSolution2('Python','typhon'));
