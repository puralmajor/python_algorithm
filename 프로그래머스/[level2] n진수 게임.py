def change(n: int, num: int) -> str:
    result = ''
    while num:
        num, mod = num // n, num % n
        if 9 < mod:
            mod = chr(mod + ord('A') - 10)
        result += str(mod)

    return result[-1::-1]


def solution(n, t, m, p):
    total = t * m
    cur = '0'
    nx = 1

    while len(cur) < total:
        cur += change(n, nx)
        nx += 1

    return cur[p - 1:(t - 1) * m + p:m]