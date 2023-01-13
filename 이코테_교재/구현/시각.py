n = int(input())
cur = [0, 0, 0]
cnt = 0
while cur != [n, 59, 59]:
    cur[2] += 1
    if cur[2] == 60:
        cur[1] += 1
        cur[2] = 0

    if cur[1] == 60:
        cur[0] += 1
        cur[1] = 0

    temp = ''.join(map(str, cur))
    if '3' in temp:
        cnt += 1

print(cnt)