from copy import deepcopy
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    ans = []

    def dfs(visited, x, y, length):
        if x == n-1 and y == m-1:
            ans.append(length+1)
            return
        if maps[x][y] == 0 or visited[x][y] == 2:
            return
        visited[x][y] = 2
        if x < n-1:
            dfs(deepcopy(visited), x+1, y, length+1)
        if x > 0:
            dfs(deepcopy(visited), x-1, y, length+1)
        if y < m-1:
            dfs(deepcopy(visited), x, y+1, length+1)
        if y > 0:
            dfs(deepcopy(visited), x, y-1, length+1)

    dfs(deepcopy(maps), 0, 0, 0)
    print(min(ans))

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])