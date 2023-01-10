import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])
