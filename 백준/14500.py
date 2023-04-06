# import sys
# from itertools import product
# from copy import deepcopy
# inp = sys.stdin.readline
#
#
# def place(x, y):
#     val = 0
#     for c in case:
#         print(c)
#         temp = paper[x][y]
#         p = deepcopy(paper)
#         nx, ny = x, y
#         visit = set()
#         visit.add((nx, ny))
#         p[nx][ny] = '.'
#         flag = False
#         for dx, dy in c:
#             nx = nx+dx
#             ny = ny+dy
#             if (nx, ny) in visit:
#                 flag = True
#                 break
#             if 0 <= nx < n and 0 <= ny < m:
#                 temp += paper[nx][ny]
#                 visit.add((nx, ny))
#                 p[nx][ny] = '.'
#             else:
#                 flag = True
#                 break
#         if not flag:
#             val = max(val, temp)
#             print(*p, sep='\n')
#             print()
#     return val
#
def last_place(x, y):
    moves = [[[0, 1], [0, 1], [-1, -1]], [[0, 1], [0, 1], [1, -1]], [[1, 0], [1, 0], [-1, 1]], [[1, 0], [1, 0], [-1, -1]]]
    val = 0
    for move in moves:
        flag = False
        nx, ny = x, y
        temp = paper[nx][ny]
        p = deepcopy(paper)
        p[nx][ny] = '.'
        for dx, dy in move:
            nx, ny = nx+dx, ny+dy

            if 0 <= nx < n and 0 <= ny < m:
                temp += paper[nx][ny]
                p[nx][ny] = '.'
            else:
                flag = True

        if not flag:
            val = max(temp, val)
            print(*p, sep='\n')
            print()

    return val
#
#
# n, m = map(int, inp().split())
# paper = [list(map(int, inp().split())) for _ in range(n)]
# answer = 0
# case = list(product([[1, 0],[-1, 0],[0, 1],[0, -1]], repeat=3))
#
# for i in range(n):
#     for j in range(m):
#         answer = max(answer, place(i, j))
#         answer = max(answer, last_place(i, j))
#
# print(answer)



# method 2.

def dfs(x, y, depth, cur):
    global answer

    if cur + max_val*(4-depth) <= answer:
        return

    if depth == 4:
        answer = max(answer, cur)
        return

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            if depth == 2:
                visit[nx][ny] = True
                dfs(x, y, depth+1, cur + paper[nx][ny])
                visit[nx][ny] = False

            visit[nx][ny] = True
            dfs(nx, ny, depth+1, cur + paper[nx][ny])
            visit[nx][ny] = False



n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = 0

visit = [[False]*m for _ in range(n)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_val = max(map(max, paper))

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i, j, 1, paper[i][j])
        visit[i][j] = False

print(answer)