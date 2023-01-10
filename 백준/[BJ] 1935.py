import sys
from collections import deque
import re
input = sys.stdin.readline

def calcualter(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        return a/b


n = int(input())
fix = deque(list(input().rstrip()))

op = {'+', '-', '/', '*'}
val = {}
for i in range(n):
    val[chr(65+i)] = int(input())

calc = []

while fix:
    cur = fix.popleft()
    if cur in op:
        b = calc.pop()
        a = calc.pop()
        calc.append(calcualter(cur, a, b))
    else:
        calc.append(val[cur])

print('%.2f' % calc[0])