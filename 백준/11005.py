import sys

n, b = map(int, sys.stdin.readline().split())
trans = {i-55:chr(i) for i in range(ord('A'), ord('Z')+1)}
answer = ''

while n:
    tmp = n%b
    if 9 < tmp:
        tmp = trans[tmp]

    answer += str(tmp)
    n = n // b

print(answer[::-1])