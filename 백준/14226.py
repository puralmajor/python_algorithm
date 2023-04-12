import sys
from collections import deque


input = sys.stdin.readline

s = int(input())
dist =[[-1] * (s+1) for _ in range(s+1)]
q = deque()
q.append((1, 0))
dist[1][0] = 0

while q:
    cur, clip = q.popleft()

    if dist[cur][cur] == -1:
        dist[cur][cur] = dist[cur][clip] + 1
        q.append((cur, cur))

    if cur+clip <= s and dist[cur+clip][clip] == -1:
        dist[cur+clip][clip] = dist[cur][clip] + 1
        q.append((cur+clip, clip))

    if cur-1 >= 0 and dist[cur-1][clip] == -1:
        dist[cur-1][clip] = dist[cur][clip] + 1
        q.append((cur-1, clip))

print(min([i for i in dist[s] if i != -1]))
