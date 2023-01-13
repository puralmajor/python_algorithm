from collections import deque


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    q = deque(routes)

    while q:
        enter, out = q.popleft()
        answer += 1
        while q and q[0][0] <= out:
            q.popleft()

    return answer