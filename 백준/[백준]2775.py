# a0i = i, 1 2 3 4 5 6 7 ...
# a1i = sigma(i), 1 3 6 10 15 22 ...
# a2i = sigma(sigma(i), 1 4 10 20 35 ...
# a3i = sigma(sigma(sigma(i))
def sigma(n, m):
    value = 0
    for i in range(n+1):
        value += m[i]
    return value


t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    answer = [i+1 for i in range(n)]
    temp = answer.copy()
    for _ in range(k):
        for j in range(1, n):
            temp[j] = sigma(j, answer)

    print(answer[len(answer)-1])
