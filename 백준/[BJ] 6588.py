import sys
input = sys.stdin.readline

def chae(n):
    sosu = [True] * (n+1)

    for i in range(2, int(n**.5)+1):
        if sosu[i]:
            for j in range(i+i, n+1, i):
                sosu[j] = False

    return [i for i in range(3, n, 2) if sosu[i]]


arr = chae(1000000)
while True:
    n = int(input())
    if n == 0:
        break

    left, right = 0, n

    while left < right:
        tmp = arr[left] + arr[right]
        if tmp == n:
            print('{} = {} + {}'.format(n, arr[left], arr[right]))
            break
        else:
            if tmp < n:
                left += 1
            else:
                right -= 1

    if arr[left]+arr[right] != n:
        print("Goldbach's conjecture is wrong.")
