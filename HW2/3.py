from sys import stdin, stdout

stdout.write("Your word : ")
word = stdin.readline()

if 'a' in word:
    index = word.index('a')
    print(word[:index + 1])
    print(word[index + 1:])
else:
    print("문자열에 'a' 가 포함되어 있지 않습니다")
