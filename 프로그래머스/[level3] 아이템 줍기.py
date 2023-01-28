def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    draw = [[0] * 11 for _ in range(11)]

    for lx, ly, rx, ry in rectangle:
        for y in range(ly, ry):
            for x in range(lx, rx):
                draw[10-y][x] = 1

    print(*draw, sep='\n')
    return answer

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)