TC = int(input())

for T in range(TC):
    n = int(input())
    base = int(n**.5)
    if base ** 2 == n:
        print(f'#{T+1} {2*(base-1)}')
    else:
        for x in range(base, 0, -1):
            if n % x == 0:
                y = n//x
                print(f'#{T + 1} {(x-1)+(y-1)}')
                break
