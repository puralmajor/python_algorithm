import sys

n, m = map(int, input().split())
pock = dict()
pock2 = dict()

for i in range(n):
    temp = input()
    pock[i+1] = temp
    pock2[temp] = i+1

for _ in range(m):
    test = input()
    if test.isdecimal():
        print(pock[int(test)])
    else:
        print(pock2[test])