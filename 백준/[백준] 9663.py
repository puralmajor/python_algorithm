n = int(input())
chess = []
ans = 0

for _ in range(n):
    chess.append([False] * n)


def dfs(t):
    global ans
    for i in range(t, n):
        if False not in chess[i]:
            ans -= 1
            continue
        chess[i] = [True] * n
        for j in range(n):
            chess[j][i] = True
            if i > j:
                chess[j][i-j] = True
            elif i < j:
                chess[j][j-i] = True

        ans += 1
        dfs(i)


dfs(0)
print(ans)