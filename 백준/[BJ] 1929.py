def chae(m, n):
    sosu = [True] * (n+1)
    sosu[0], sosu[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if sosu[i]:
            for j in range(2*i, n+1, i):
                sosu[j] = False

    return [i for i in range(m, n+1) if sosu[i]]


a, b = map(int, input().split())
print(*chae(a, b), sep='\n')