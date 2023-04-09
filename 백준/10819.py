from itertools import permutations

n = int(input())
answer = 0
for i in permutations(map(int, input().split()), n):
    temp = 0
    for j in range(n-1):
        temp += abs(i[j]-i[j+1])

    answer = max(temp, answer)

print(answer)