def dfs(cur, depth=0):
    if depth == 4:
        return True

    visit[cur] = True

    for nx in relation[cur]:
        if not visit[nx]:
            flag = dfs(nx, depth+1)
            if flag:
                return True

    visit[cur] = False
    return False


n, m = map(int, input().split())
relation = [[] for _ in range(n)]
ans = 0
for _ in range(m):
    v, w = map(int, input().split())
    relation[v].append(w)
    relation[w].append(v)


for i in range(n):
    visit = [False] * n
    ans = dfs(i)
    if ans:
        break

print(int(ans))