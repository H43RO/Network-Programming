from sys import stdin


def solve(small, big):
    while small > 0:
        temp = big % small
        big = small
        small = temp

    return big


a, b = map(int, stdin.readline().split())

# 큰 수, 작은 수를 구분하여 저장
if a < b:
    small = a
    big = b
else:
    small = b
    big = a


# 최대 공약수 출력
print(solve(small, big))
