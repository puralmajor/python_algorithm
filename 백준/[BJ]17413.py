import sys
from collections import deque

s = deque(sys.stdin.readline().strip())
common = deque()
answer = ''
while s:
    cur = s.popleft()
    if cur == '<':
        answer += ''.join(common)
        common = deque()
        answer += cur
        while s[0] != '>':
            answer += s.popleft()
        answer += s.popleft()
    elif cur == ' ':
        common.append(cur)
        answer += ''.join(common)
        common = deque()
    else:
        common.appendleft(cur)

if common:
    answer += ''.join(common)

print(answer)