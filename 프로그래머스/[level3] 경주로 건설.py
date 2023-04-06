def solution(board):
    n = len(board)
    cost = [[float('inf')] * n for _ in range(n)]
    cost[0][0] = 0

    for i in ('x', 'y'):
        def dfs(x, y, direct, n, depth=0):
            if visit[x][y]:
                return

            visit[x][y] = True
            print(x, y)

            for i in range(2):
                nx, ny = x + (-1) ** i, y + (-1) ** i

                if direct == 'x':
                    if 0 <= nx < n and board[nx][y] != 1 and not visit[nx][y]:
                        cost[nx][y] = min(cost[nx][y], cost[x][y] + 100)
                        dfs(nx, y, 'x', n, depth+1)
                        visit[nx][y] = False

                    if 0 <= ny < n and board[x][ny] != 1 and not visit[x][ny]:
                        cost[x][ny] = min(cost[x][y] + 600, cost[x][ny])
                        dfs(x, ny, 'y', n, depth+1)
                        visit[x][ny] = False

                else:
                    if 0 <= ny < n and board[x][ny] != 1 and not visit[x][ny]:
                        cost[x][ny] = min(cost[x][y] + 100, cost[x][ny])
                        dfs(x, ny, 'y', n, depth + 1)
                        visit[x][ny] = False

                    if 0 <= nx < n and board[nx][y] != 1 and not visit[nx][y]:
                        cost[nx][y] = min(cost[nx][y], cost[x][y] + 600)
                        dfs(nx, y, 'x', n, depth + 1)
                        visit[nx][y] = False



        visit = [[False] * n for _ in range(n)]
        dfs(0, 0, i, n)
        visit[0][0] = False

    return cost[n-1][n-1]


b = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(b))