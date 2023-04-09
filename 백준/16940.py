n = int(input())
graph = [set() for _ in range(n+1)]

for _ in range(n-1):
    v, w = map(int, input().split())
    graph[v].add(w)
    graph[w].add(v)

target = tuple(map(int, input().split()))
if target[0] != 1:
    print(0)
    exit()

order = [set() for _ in range(n)]
order[0] = graph[1]
visit = set()
visit.add(1)
rank = 0
for i in range(1, n):
    if order[rank]:
        if target[i] not in order[rank]:
            print(0)
            exit()
        else:
            order[rank].remove(target[i])

    if not order[rank]:
        rank += 1
    visit.add(target[i])
    order[i] = graph[target[i]] - visit

print(1)

