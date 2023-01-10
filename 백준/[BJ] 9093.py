import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    words = list(input().split())
    answer = ''
    for i in words:
        answer += i[::-1] + ' '
    print(answer)