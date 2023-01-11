def solution(board):
    answer = 0
    n = len(board)
    board2 = [[0]*(n+2) for _ in range(n+2)] 
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board2[i][j] = 1
                board2[i][j-1] = 1
                board2[i][j+1] = 1
                board2[i-1][j-1] = 1
                board2[i-1][j] = 1
                board2[i-1][j+1] = 1
                board2[i+1][j-1] = 1
                board2[i+1][j] = 1
                board2[i+1][j+1] = 1
    board2 = [board2[i][1:n] for i in range(1, n)]
    for i in board2:
        answer += sum(i)
    return answer