def solution(board, aloc, bloc):
    answer = 0
    X, Y = len(board), len(board[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while True:
        for i in range(4):
            nx, ny = aloc[0] + dx[i], aloc[1] + dy[i]
            if nx < X and ny < Y and board[nx][ny] == 1:
                board[aloc[0]][aloc[1]] = 0
                aloc = [nx, ny]
                answer += 1
                break
        else:
            break

        for i in range(4):
            nx, ny = bloc[0] + dx[i], bloc[1] + dy[i]
            if nx < X and ny < Y and board[nx][ny] == 1:
                board[bloc[0]][bloc[1]] = 0
                bloc = [nx, ny]
                answer += 1
                break
        else:
            break

    return answer


bd = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
a = [1, 0]
b = [1, 2]

print(solution(bd, a, b))