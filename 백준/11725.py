from collections import deque
def bfs():
    q = deque()
    q.append(1)

    while q:
        cur = q.popleft()
        if visit[cur]:
            continue
        visit[cur] = True
        for i in tree[cur]:
            if not visit[i]:
                parent[i] = cur
                q.append(i)


n = int(input())
tree = [[] for _ in range(n+1)]
visit = [False] * (n+1)
parent = [None] * (n+1)
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

bfs()
print(*parent[2:], sep='\n')
