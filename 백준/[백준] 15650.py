n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

def dfs(num):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(num, n+1):
            if visited[i]:
                continue
            visited[i] = True
            s.append(i)
            dfs(i)
            s.pop()
            visited[i] = False

dfs(1)