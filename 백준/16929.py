n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = set()
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
