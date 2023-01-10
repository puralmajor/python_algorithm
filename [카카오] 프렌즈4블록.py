def solution(m, n, board):
    answer = 0
    b = [list(i) for i in board]
    print(b)
    stack = []
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1] != 0:
                    stack.append([[i,j], [i+1,j], [i,j+1], [i+1, j+1]])

        for i in stack:
            for j in i:
                b[j[0]][j[1]] = 0
                answer += 1
            answer /= 4

        for i in range(m - 1):
            for j in range(n - 1):
                if b[i][j] == 0 and
    print(b)

    return answer


a = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(4, 5, a)
