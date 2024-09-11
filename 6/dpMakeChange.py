def dpMakeChange(coinList, change,coinused):
    mincoins = [0] * (change + 1)
    newcoin = 1;
    for cent in range(1, change + 1):
        coinCount = cent
        for i in [c for c in coinList if c <= cent]:
            if mincoins[cent - i] + 1 < coinCount:
                coinCount = mincoins[cent - i] + 1;
                newcoin = i;
        mincoins[cent] = coinCount;
        coinused[cent] = newcoin;
    return mincoins[change];

def printCoins(coinused, change):
    coin = change;
    while coin > 0:
        thiscoin = coinused[coin];
        print(thiscoin);
        coin = coin-thiscoin

print (dpMakeChange([1,5,10,21,25,50], 63))