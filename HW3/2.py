from sys import stdin

d = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
     {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
     {'name': 'Princess', 'phone': '555=3141', 'email': ''},
     {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

print("==========지시사항 1번==========")
for x in d:
    if x['phone'].endswith('8'):
        print(x['name'])

print("==========지시사항 2번==========")
for x in d:
    if x['email'] == '':
        print(x['name'])

user = stdin.readline().strip()
found = False
for x in d:
    if x['name'] == user:
        print(x['phone'], x['email'])
        found = True
if not found:
    print('이름이 없습니다')