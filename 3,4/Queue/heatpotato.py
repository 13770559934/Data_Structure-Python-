from Queue import Queue;

def heatpotato(namelist, num):
    simqueue = Queue();
    for name in namelist:
        simqueue.enqueue(name);

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue());

        simqueue.dequeue();

    return simqueue.dequeue();

print(heatpotato(['Roy','hhh','else','luci','Ethan','Joey','Mac'], 10));