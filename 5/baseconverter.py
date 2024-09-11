def toStr(n, base):
    convertingstr = '0123456789ABCDEF'
    if n < base:
        return convertingstr[n];
    else:
        return toStr(n//base,base)+ convertingstr[n%base];

print(toStr(100,16))