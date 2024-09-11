from zoneinfo import available_timezones
from Queue import Queue;
import random;

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm;
        self.currentTask = None;
        self.timeRemaining = 0;

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1;
            if self.timeRemaining <= 0:
                self.currentTask = None;

    def busy(self):
        if self.currentTask == None:
            return False;

        else:
            return True;

    def startNext(self, task_obj):
        self.currentTask = task_obj;
        self.timeRemaining = task_obj.getPages() * 60 / self.pagerate;


class Task:
    def __init__(self, time):
        self.timeStamp = time;
        self.page = random.randrange(1,20)

    def getPages(self):
        return self.page;

    def getStamp(self):
        return self.timeStamp;

    def waitTime(self, currenttime):
        return currenttime -self.timeStamp

def newPrintTask():
    num = random.randrange(1,181);
    if num == 180:
        return True;
    else:
        return False;

def simulation(numSeconds, ppm):
    printer = Printer(ppm);
    printqueue = Queue();
    waittimelist = [];

    for currentsecond in range(numSeconds):
        if newPrintTask():
            newtask = Task(currentsecond);
            printqueue.enqueue(newtask);
        
        if not(printer.busy()) and not(printqueue.isEmpty()):
            nexttask = printqueue.dequeue();
            waittimelist.append(newtask.waitTime(currentsecond));
            printer.startNext(nexttask);

        printer.tick();

    averageWait = sum(waittimelist) / len(waittimelist);

    print(averageWait,printqueue.size());


for i in range(10):
    simulation(3600, 10);

