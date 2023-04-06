from collections import deque

k = int(input())

for _ in range(k):
    u, v = map(int, input().split())
    graph = [[] for _ in range(u)]
    for _ in range(v):
        s, e = map(int, input().split())
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)

    visit = set(range(u))
    count = 0
    idx = 0

    while True:
        q = deque()
        q.append(idx)
        visit.remove(idx)

        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if i in visit:
                    q.append(i)
                    visit.remove(i)

        count += 1
        if count > 2:
            break

        if visit:
            idx = visit.pop()
        else:
            break

