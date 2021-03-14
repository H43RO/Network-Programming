from sys import stdout

for i in range(1, 1001):
    stdout.write(f"{str(i).zfill(4)} 의 각 자릿수 합 : ")
    print(sum(list(map(int, str(i)))))
