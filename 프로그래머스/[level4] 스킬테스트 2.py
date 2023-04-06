def solution(rc, operations):
    n, m = len(rc), len(rc[0])

    for op in operations:
        if op == 'ShiftRow':
            rc = [rc[-1]] + rc[:-1]
            print('shift')

        elif op == 'Rotate':
            print('rotate')
            temp = [[0] * m for _ in range(n)]
            for i in range(n):
                if i == 0:
                    temp[i] = [rc[i + 1][0]] + rc[i][:-1]
                elif i == n - 1:
                    temp[i] = rc[i][1:] + [rc[i - 1][-1]]
                else:
                    temp[i] = [rc[i + 1][0]] + rc[i][1:-1] + [rc[i - 1][-1]]
            rc = temp

        print(*rc, sep='\n')

    return rc

rc =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operation =["Rotate", "ShiftRow"]
print(solution(rc, operation))