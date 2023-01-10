import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
cnt = 1


def dfs(r):
    global cnt
    if visited[r-1]:
        return

    visited[r-1] = cnt
    cnt += 1
    for i in graph[r]:
        if not visited[i-1]:
            dfs(i)


input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = defaultdict(list)
visited = [0] * n
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1,n+1):
    graph[i] = sorted(graph[i])

dfs(r)
for i in visited:
    print(i)
