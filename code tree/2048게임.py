from copy import deepcopy
def dfs(head, board, depth=1):
    global answer

    if head == 'L':
        for i in range(n):
            mix = set()
            for j in range(1, n):
                if board[i][j] != 0:
                    for k in range(j - 1, -1, -1):
                        if board[i][j] == board[i][k] and (i, k) not in mix:
                            board[i][k] *= 2
                            mix.add((i, k))
                            board[i][j] = 0
                            break
                        elif board[i][k] != 0:
                            if k + 1 != j:
                                board[i][k + 1], board[i][j] = board[i][j], 0
                            break
                    else:
                        board[i][0], board[i][j] = board[i][j], 0

    if head == 'R':
        for i in range(n):
            mix = set()
            for j in range(n - 2, -1, -1):
                if board[i][j] != 0:
                    for k in range(j + 1, n):
                        if board[i][j] == board[i][k] and (i, k) not in mix:
                            board[i][k] *= 2
                            mix.add((i, k))
                            board[i][j] = 0
                            break
                        elif board[i][k] != 0:
                            if k - 1 != j:
                                board[i][k - 1], board[i][j] = board[i][j], 0
                            break
                    else:
                        board[i][n - 1], board[i][j] = board[i][j], 0

    if head == 'U':
        for j in range(n):
            mix = set()
            for i in range(1, n):
                if board[i][j] != 0:
                    for k in range(i - 1, -1, -1):
                        if board[i][j] == board[k][j] and (k, j) not in mix:
                            board[k][j] *= 2
                            mix.add((k, j))
                            board[i][j] = 0
                            break
                        elif board[k][j] != 0:
                            if k + 1 != i:
                                board[k + 1][j], board[i][j] = board[i][j], 0
                            break
                    else:
                        board[0][j], board[i][j] = board[i][j], 0

    if head == 'D':
        for j in range(n):
            mix = set()
            for i in range(n - 2, -1, -1):
                if board[i][j] != 0:
                    for k in range(i + 1, n):
                        if board[i][j] == board[k][j] and (k, j) not in mix:
                            board[k][j] *= 2
                            mix.add((k, j))
                            board[i][j] = 0
                            break
                        elif board[k][j] != 0:
                            if k - 1 != i:
                                board[k - 1][j], board[i][j] = board[i][j], 0
                            break
                    else:
                        board[n - 1][j], board[i][j] = board[i][j], 0

    if depth == 5:
        cur = max(map(max, board))
        answer = max(answer, cur)
        return

    for nx in ['L', 'R', 'U', 'D']:
        dfs(nx, deepcopy(board), depth + 1)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for H in ['L', 'R', 'U', 'D']:
    dfs(H, deepcopy(board))

print(answer)