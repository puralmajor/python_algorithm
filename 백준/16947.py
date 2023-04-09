def dfs(v, stack=set(), before=None):
    if v in visited:
        return False
    if v in stack:
        for i in stack:
            cycle.add(i)
        return True

    visited.add(v)
    stack.add(v)
    for w in station[v]:
        if w == before:
            continue

        elif w in stack:
            for i in stack:
                cycle.add(i)
            return True

        elif w in visited:
            continue

        dfs(w, stack.copy(), v)


def access(i, depth = 0):
    if i in accessed:
        return

    if i in cycle:
        return

    accessed.add(i)

    for j in station[i]:
        if j in cycle:
            arr[i] = depth+1
            break

        if j not in accessed:
            access(j, depth+1)


n = int(input())
station = [[] for _ in range(n)]

for _ in range(n):
    v, w = map(int, input().split())
    station[v-1].append(w-1)
    station[w-1].append(v-1)


visited = set()
cycle = set()
for i in range(n):
    if i not in visited:
        dfs(i)

arr = [0] * n
print(cycle)
for i in range(n):
    if i not in cycle:
        accessed = set()
        access(i)

print(*arr)