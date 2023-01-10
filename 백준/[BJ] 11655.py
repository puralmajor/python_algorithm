import sys

s = list(sys.stdin.readline().rstrip())
answer = ''

for i in s:
    if i.islower():
        tmp = ord(i) + 13
        if tmp > ord('z'):
            tmp = ord('a') + (tmp % ord('z')) - 1
        answer += chr(tmp)

    elif i.isupper():
        tmp = ord(i) + 13
        if tmp > ord('Z'):
            tmp = ord('A') + tmp % ord('Z') - 1
        answer += chr(tmp)

    else:
        answer += i

print(answer)