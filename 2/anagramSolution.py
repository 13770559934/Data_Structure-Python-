import time;

def anagramSolution(s1, s2):
    start = time.time();
    list1 = list(s1.lower());
    list2 = list(s2.lower());
    if len(list1) != len(list2):
        return ("Two words must have the same length!!");
    for i in list1:
        found = False;
        for j in range(len(list2)):
            if i == list2[j]:
                list2[j] = None;
                found = True
                
        if not found:
            end = time.time()
            return (False, end - start);
        end = time.time()
            
    return (True, end - start)





print("%s, %10.7f"
    %anagramSolution('python', "typhon"))
                
                
