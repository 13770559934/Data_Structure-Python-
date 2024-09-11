from Dequeue import Dequeue;

def palchecker(astring):
    temp_dequeue = Dequeue();

    for ch in astring:
        temp_dequeue.addfront(ch);

    stillEqual = True;

    while stillEqual and temp_dequeue.size() > 1:
        first = temp_dequeue.removefront();
        last = temp_dequeue.removerear();
        if first != last:
            stillEqual = False;

    return stillEqual;

print(palchecker('safnliksueh'));
print(palchecker('radar'));