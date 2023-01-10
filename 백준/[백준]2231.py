n = int(input())
min_answer = abs(n - (len(str(n)*9)))

for i in range(min_answer, n):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == n:
        print(i)
        break
else:
    print(0)