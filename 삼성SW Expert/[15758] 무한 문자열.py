def LCM(a, b):
    for i in range(min(a, b), a*b+1):
        if i % a == 0 and i % b == 0:
            return i

    return a*b


n = int(input())

for i in range(n):
    S, T = input().split()
    idx = 0
    s, t = len(S), len(T)
    lcm = LCM(s, t)

    S = S * (lcm//s)
    T = T * (lcm//t)

    if S != T:
        print(f"#{i+1} no")
    else:
        print(f"#{i+1} yes")