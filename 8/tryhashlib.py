import hashlib;

print(hashlib.md5("hello world!".encode('utf-8')).hexdigest())
