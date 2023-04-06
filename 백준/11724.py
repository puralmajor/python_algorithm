import sys
sys.setrecursionlimit(10000)


def dfs(x):
    if visit[x]:
        return

    visit[x] = True
    nodes.remove(x)
    for i in graph[x]:
        if not visit[i]:
            visit
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
answer = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visit = [False] * n
idx = 0
nodes = set(range(1, n))

while True:
    dfs(idx)
    answer += 1

    if nodes:
        idx = nodes.pop()
    else:
        break

print(answer)