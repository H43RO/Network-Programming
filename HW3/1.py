from sys import stdin

days = {'January': 31, 'February': 28, 'March': 31,
        'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30,
        'October': 31, 'November': 30, 'December': 31}

print("==========지시사항 1번==========")
user = stdin.readline().strip()
print(days[user])
print("==========지시사항 2번==========")
print(sorted(list(days.keys())))
print("==========지시사항 3번==========")
for x in days.items():
    if x[1] == 31:
        print(x[0], end=' ')
print()
print("==========지시사항 4번==========")
print(sorted(days.items(), key=lambda x: x[1]))
print("==========지시사항 5번==========")
user = stdin.readline().strip()
for x in days.items():
    if x[0].startswith(user):
        print(x[1])
