def transform(string):
    string = list(string.split(sep='&'))
    data = dict()
    for x in string:
        key, value = x.split(sep='=')
        data[key] = value
    return data


print(transform(string=input().strip()))
