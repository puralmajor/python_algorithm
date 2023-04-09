n = int(input())
tree = [set() for _ in range(n+1)]

for _ in range(n-1):
    v, w = map(int, input().split())
    tree[v].add(w)
    tree[w].add(v)

root = tuple(map(int, input().split()))

if root[0] != 1:
    print(0)
    exit()

visit = [False] * (n+1)
visit[1] = True

for i in range(n-1):
    all_visit = True
    for j in tree[root[i]]:
        if not visit[j]:
            all_visit = False
            break

    if root[i+1] not in tree[root[i]] and not all_visit:
        print(0)
        exit()
    visit[root[i]] = True

print(1)