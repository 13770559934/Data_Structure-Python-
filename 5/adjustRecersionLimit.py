import sys;
print(sys.getrecursionlimit())#找到python的递归深度
sys.setrecursionlimit(3000); #改变递归深度
print(sys.getrecursionlimit())