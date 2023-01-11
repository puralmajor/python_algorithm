n = int(input())
i = 2
while n:
    if n == 1:
        break
    if n%i == 0:
        print(i)
        n = n//i
    else:
        i += 1