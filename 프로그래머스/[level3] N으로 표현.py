def solution(N, number):
    dp = [None]
    dp.append(set(N))
    if N == number:
        return 1

    return -1