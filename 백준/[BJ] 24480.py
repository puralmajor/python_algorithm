import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
cnt = 1


def dfs(cur):
    global cnt
    if visited[cur-1]:
        return

    visited[cur-1] = cnt
    cnt += 1

    for x in graph[cur]:
        if visited[x-1] == 0:
            dfs(x)


n, m, r = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [0] * n

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n+1):
    graph[i] = sorted(graph[i], reverse=True)

dfs(r)
for i in visited:
    print(i)
