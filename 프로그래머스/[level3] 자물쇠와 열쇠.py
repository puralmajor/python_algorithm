# 딱 포개질 필요는 없음 그냥 빈 부분만 채울 수 있는지 확인하면 됨
def rotate(arr):
    return list(map(list, zip(*arr[::-1])))


def solution(key, lock):
    n = len(lock)
    m = len(key)

    def check(x, y, n, m):
        for i in range(x, n):
            if x - i >= m:
                break
            for j in range(y, n):
                if j - y >= m:
                    break
                if key[i - x][j - y] == lock[i][j] == 1:
                    return False
                elif key[i - x][j - y] == 0 and lock[i][j] == 0:
                    return False

        return True

    for i in range(n):
        for j in range(n):
            for t in range(4):
                key = rotate(key)
                if check(i, j, n, m):
                    return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))