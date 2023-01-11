import sys
input = sys.stdin.readline

def get_prime(n):

    a = [True] * (n+1)
    a[0] = False
    a[1] = False

    for i in range(2, int(n**.5)+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False

    return a


primes = get_prime(10**6)


T = int(input())

for _ in range(T):
    n = int(input())
    answer = 0 if n != 4 else 1
    for i in range(3, n//2+1):
        if primes[i] and primes[n-i]:
            answer += 1

    print(answer)