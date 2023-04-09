n = input()
cur = 1
answer = 0
while cur < len(n):
    answer += cur * (10**cur - 10**(cur-1))
    cur += 1

answer += cur * (int(n) - 10**(cur-1) + 1)
print(answer)