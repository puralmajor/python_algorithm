from collections import Counter


def solution(n, works):
    answer = 0
    count = Counter(works)
    m = max(count.keys())

    for i in range(m, 0, -1):
        if count[i] > n:
            count[i] -= n
            count[i - 1] += n
            n = 0
        else:
            n -= count[i]
            count[i - 1] += count[i]
            del count[i]

        if n == 0:
            break

    for i in count.keys():
        answer += (i ** 2) * count[i]

    return answer