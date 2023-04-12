def dfs():



n = int(input())
graph = [[] for _ in range(n+1)]
ans = 0
for _ in range(n):
    temp = list(map(int, input().split()))
    v = temp[0]

    for i in range(1, len(temp)-1, 2):
        w, dt = temp[i], temp[i+1]
        graph[v].append((w, dt))

