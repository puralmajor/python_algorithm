n = int(input())
ws = []
for i in range(n):
    temp = list(map(int, input().split()))
    temp.append(i)
    temp.append(1)
    ws.append(temp)

weight_sorted = sorted(ws)

for i in range(len(weight_sorted)):
    for j in range(i+1, len(weight_sorted)):
        if weight_sorted[i][0] < weight_sorted[j][0] and weight_sorted[i][1] < weight_sorted[j][1]:
            weight_sorted[i][3] += 1

ans = sorted(weight_sorted, key=lambda x: x[2])
for i in ans:
    print(i[3], end=' ')