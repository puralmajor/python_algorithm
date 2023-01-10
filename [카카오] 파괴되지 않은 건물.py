def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[1])
    skill_sum = [[0 for _ in range(m)] for _ in range(n)]

    for i in skill:
        if i[0] == 1:
            for j in range(i[1], i[3]+1):
                for k in range(i[2], i[4]+1):
                    board[j][k] -= i[5]
        else:
            for j in range(i[1], i[3]+1):
                for k in range(i[2], i[4]+1):
                    board[j][k] += i[5]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0 :
                answer += 1

    return answer


a=[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
b = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
solution(a,b)