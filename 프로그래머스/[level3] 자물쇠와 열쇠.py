def rotate(arr):
    holes = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                holes.append((i, j))

    return [holes, list(map(list, zip(*arr[::-1])))]

def solution(key, lock):
    n = len(lock)
    m = len(key)
    if sum(map(sum, key)) < n ** 2 - sum(map(sum, lock)):
        return False

    holes = []
    for i in range(4):
        hole, key = rotate(key)
        holes.append(hole)

    target = []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                target.append((i, j))

    return False


k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(k, l))