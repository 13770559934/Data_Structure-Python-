import time;

def anagramSolution3(s1, s2):
    start = time.time()
    s1 = s1.lower();
    s2 = s2.lower();

    c1 = [0]*26;
    c2 = [0]*26;

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a');
        c1[pos] += 1;
    for j in range(len(s2)):
        pos = ord(s2[j]) - ord('a');
        c2[pos] += 1;

    stillOk = True;
    z = 0;
    while z < 26 and stillOk:
        if c1[z] != c2[z]:
            stillOk = False;
        else:
            z += 1;
    end = time.time()
    return (stillOk, end - start);

print("%s, %10.7f"
    %anagramSolution3('Python','typhon'));
