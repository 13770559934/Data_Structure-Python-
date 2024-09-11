import list_test;
import timeit;

t1 = timeit.Timer('list_test.test1()', 'import list_test');
print (type(t1));
print ('concat %f seconds\n'
    %t1.timeit(number = 1000));

t2 = timeit.Timer('list_test.test2()', 'import list_test');
print ('append %f seconds\n'
    %t2.timeit(number = 1000));

t3 = timeit.Timer('list_test.test3()', 'import list_test');
print ('comprehension %f seconds\n'
    %t3.timeit(number = 1000));

t4 = timeit.Timer('list_test.test4()', 'import list_test');
print ('list range %f seconds\n'
    %t4.timeit(number = 1000));
