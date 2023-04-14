from collections import deque


def move(board, x, y, d):
    if d == 'U':

        for i in range(x-1, -1, -1):
            if board[i][y] == 'D':
                return (i + 1, y)

        return (0, y)

    elif d == 'D':
        for i in range(x + 1, len(board)):
            if board[i][y] == 'D':
                return (i - 1, y)
        return (len(board)-1, y)

    elif d == 'R':
        for j in range(y + 1, len(board[0])):
            if board[x][j] == 'D':
                return (x, j - 1)
        return (x, len(board[0])-1)

    elif d == 'L':
        for j in range(y-1, -1, -1):
            if board[x][j] == 'D':
                return (x, j + 1)
        return (x, 0)

    return (x, y)


def solution(board):
    r = len(board)
    c = len(board[0])
    start = []
    goal  = []
    for i in range(len(board)):
        if not start:
            temp = board[i].find('R')
            if temp != -1:
                start = [i, temp]

        if not goal:
            temp = board[i].find('G')
            if temp != -1:
                goal = [i, temp]

        if start and goal:
            break

    if goal[0] != r-1 and goal[1] != c-1:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = goal[0] + dx, goal[1] + dy
            if board[nx][ny] == 'D':
                break
        else:
            return -1

    q = deque()
    q.append((*start, 0))
    visit = set()

    while q:
        x, y, dist = q.popleft()
        visit.add((x, y))
        if board[x][y] == 'G':
            return dist

        for m in ('U', 'D', 'R', 'L'):
            nx = move(board, x, y, m)
            if nx not in visit:
                q.append((*nx, dist + 1))

    return -1


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))