# 딱 포개질 필요는 없음 그냥 빈 부분만 채울 수 있는지 확인하면 됨
def rotate(arr):
    return list(map(list, zip(*arr[::-1])))


def solution(key, lock):
    # check 바깥에 0이 존재하는 경우, check으로 판독 불가
    def check(x, y, n, m):
        for i in range(x):
            for j in range(n):
                if lock[i][j] == 0:
                    return False

        for j in range(y):
            for i in range(n):
                if lock[i][j] == 0:
                    return False

        for i in range(x, n):
            if i - x >= m:
                break
            for j in range(y, n):
                if j - y >= m:
                    break
                if key[i - x][j - y] == lock[i][j]:
                    return False

        return True

    n = len(lock)
    m = len(key)
    if sum(map(sum, key)) < n ** 2 - sum(map(sum, lock)):
        return False

    for i in range(n):
        for j in range(n):
            for t in range(4):
                key = rotate(key)
                if check(i, j, n, m):
                    return True
    return False