import sys
from collections import deque
fix = deque(sys.stdin.readline().rstrip())
alp = []
op = []
flag = 0
while fix:
    cur = fix.popleft()
    if cur.isalpha():
        alp.append(cur)
    else:
        op.append(cur)
        