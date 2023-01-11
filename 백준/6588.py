import sys
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

while True:
    x = int(sys.stdin.readline())
    if x == 0:
        break

    for i in range(3, len(primes)):
        if primes[i] and primes[x-i]:
            print('{} = {} + {}'.format(x, i, x-i))

    else:
        print("Goldbach's conjecture is wrong.")
