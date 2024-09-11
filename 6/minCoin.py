import time
from tracemalloc import start;
def recMC(coinList, change,knownresult):
    minCoin = change;
    if change in coinList:
        knownresult[change] = 1;
        return 1;

    elif knownresult[change] > 0:
        return knownresult[change];

    else:
        for i in [c for c in coinList if c <= change]:
            numCoin = 1 + recMC( coinList ,change-i, knownresult);

            if numCoin < minCoin:
                minCoin = numCoin;
                knownresult[change] = minCoin

        return minCoin

start = time.time()
print(recMC([1,3,10,25,33],63,[0]*64))
end = time.time()

print(end - start)