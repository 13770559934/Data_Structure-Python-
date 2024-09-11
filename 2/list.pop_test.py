import timeit;


popzero = timeit.Timer("x1.pop(0)",'from __main__ import x1');
popend = timeit.Timer("x1.pop()",'from __main__ import x1');

for i in range(1000,10000001,10000):
    x1 = list(range(i));
    pz = popzero.timeit(number = 1000);
    x1 = list(range(i));
    pe = popend.timeit(number = 1000);
    print("%10.7f,%10.7F"
          %(pz,pe))
