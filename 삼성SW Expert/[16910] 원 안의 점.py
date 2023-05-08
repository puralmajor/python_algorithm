t = int(input())

for x in range(t):
    r = int(input())
    cnt = 0
    for i in range(1, r):
        j = int((r**2 - i **2)**.5)
        cnt += j*2 + 1
    cnt *= 2
    cnt += 2 + 2*r+1
    print(f'#{x+1} {cnt}')