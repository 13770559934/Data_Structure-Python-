import time;

def sumof(i):
    start =  time.time()
    thesum = 0;
    for x in range(1,i+1):
        thesum += x
    end = time.time()

    return (thesum, end - start)

for i in range(5):
    print("The sum is %i \nRuntime is %10.7f"
        %sumof(10000));
