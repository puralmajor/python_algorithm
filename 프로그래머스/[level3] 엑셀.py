import re


def solution(commands):
    answer = []
    cells = [[''] * 5 for _ in range(5)]

    for l in commands:
        print(*cells, sep='\n')
        print('\n\n\n')
        cmd = l.split(' ')
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                r, c, val = cmd[1:]
                r, c = int(r), int(c)
                while type(cells[r][c]) == list:
                    r, c = cells[r][c][0], cells[r][c][1]
                cells[r][c] = val
            else:
                val1, val2 = cmd[1:]

                for i in range(len(cells)):
                    for j in range(len(cells[i])):
                        if cells[i][j] == val1:
                            cells[i][j] = val2

        elif cmd[0] == 'MERGE':
            r1, c1, r2, c2 = list(map(int, cmd[1:]))
            if cells[r1][c1] == '':
                cells[r1][c1] = cells[r2][c2]

            cells[r2][c2] = [r1, c1]

        elif cmd[0] == 'UNMERGE':
            r, c = cmd[1:]
            r, c = int(r), int(c)

        elif cmd[0] == 'PRINT':
            r, c = cmd[1:]
            r, c = int(r), int(c)
            p = cells[r][c]
            while type(p) == list:
                p = cells[p[0]][p[1]]
            answer.append(p)

    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
