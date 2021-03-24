from sys import stdin

data = dict()
string = list(stdin.readline().strip().split(sep='&'))
for x in string:
    key, value = x.split(sep='=')
    data[key] = value
print(data)
