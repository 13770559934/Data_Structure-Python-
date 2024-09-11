def test1():
    l = [];
    for i in range(1000):
        l = l + [i];
    return l;

def test2():
    l = [];
    for i in range(1000):
        l.append(i);
    return l;

def test3():
    return [i for i in range(1000)];

def test4():
    return list(range(1000));
