from collections import defaultdict


def solution(dirs):
    answer = 0
    visited = defaultdict(set)
    cur_x, cur_y = 0, 0
    for i in dirs:
        if i == 'U':
            if 4 < cur_x:
                continue
            if (cur_x, cur_y) not in visited[(cur_x + 1, cur_y)]:
                visited[(cur_x, cur_y)].add((cur_x + 1, cur_y))
            cur_x += 1

        if i == 'D':
            if cur_x < -4:
                continue
            if (cur_x, cur_y) not in visited[(cur_x - 1, cur_y)]:
                visited[(cur_x, cur_y)].add((cur_x - 1, cur_y))
            cur_x -= 1

        if i == 'R':
            if 4 < cur_y:
                continue
            if (cur_x, cur_y) not in visited[(cur_x, cur_y + 1)]:
                visited[(cur_x, cur_y)].add((cur_x, cur_y + 1))
            cur_y += 1

        if i == 'L':
            if cur_y < -4:
                continue
            if (cur_x, cur_y) not in visited[(cur_x, cur_y - 1)]:
                visited[(cur_x, cur_y)].add((cur_x, cur_y - 1))
            cur_y -= 1

        print(i, cur_x, cur_y,visited)

    for i in visited.keys():
        answer += len(visited[i])
    return answer

solution('LLRRL')