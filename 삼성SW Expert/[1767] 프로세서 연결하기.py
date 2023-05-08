def connect(idx, board, visit):
    if visit[idx]:
        return

    visit[idx] = True
    x, y = cores[idx]


T = int(input())


for _ in range(T):
    n = int(input())
    board = []
    cores = []
    for i in range(n):
        line = list(map(int, input().split()))
        board.append(line)
        for j in range(n):
            if line[j] == 1:
                if i != 0 and j != 0:
                    cores.append((i, j))

    answer = [0, 0] # [연결된 core 개수, 연결된 전선 길이]

    for idx in range(len(cores)):
        visit = [False]*len(cores)
        visit[idx] = True
        connect(idx, board.copy(), visit.copy())