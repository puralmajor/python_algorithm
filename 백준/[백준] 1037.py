n = int(input())
real = list(map(int, input().split()))

if n == 1:
    print(real[0]**2)
else:
    real = sorted(real)
    print(real[0]*real[len(real)-1])
