def factorize(n):
    d = 2
    cnt = 0
    while d <= n:
        if n % d == 0:
            n = n // d
            cnt += 1
        else:
            d += 1

    return cnt


def prime(n):
    arr = [True for _ in range(n+1)]
    arr[0] = False
    arr[1] = False

    for i in range(2, int(n**.5)+1):
        if arr[i]:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1

    return [x for x in range(2, n+1) if arr[x]]


a, b = map(int, input().split())
answer = 0
primes = set(prime(b))
for i in range(a, b+1):
    if i in primes:
        continue
    if factorize(i) in primes:
        answer += 1

print(answer)