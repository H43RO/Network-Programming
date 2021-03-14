from random import randint
from sys import stdin, stdout

money = 50

while True:
    coin = randint(1, 2)
    stdout.write("앞면 (1) , 뒷면 (2) 를 선택하세요 : ")
    user_input = int(stdin.readline())

    if user_input != 1 and user_input != 2:
        stdout.write("잘못된 입력입니다.\n")
        continue

    if coin == user_input:
        stdout.write("맞췄습니다! $9 를 획득합니다. ")
        money += 9
    else:
        stdout.write("틀렸습니다! $10 를 잃습니다. ")
        money -= 10

    if money < 0:
        stdout.write("돈을 모두 잃어 게임을 종료합니다.\n")
        break
    if money > 100:
        stdout.write("$100 을 획득하여 게임을 종료합니다.\n")
        break

    stdout.write(f"(현재 ${money} 보유)\n")
