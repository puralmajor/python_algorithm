n = list(map(int, input()))
m = int(input())
avail = set([i for i in range(10)])
if m:
    avail -= set(map(int, input().split()))

cur = [0]
if n == [1, 0, 0]:
    print(0)
    exit()

for i in list(avail):
    if abs(n[0] - i) < abs(n[0]-cur[0]):
        cur[0] = i

for i in range(1, len(n)):
    # if n[i] in avail:
    #     cur.append(n[i])
    #     continue

    save = 100
    chk = 0
    while chk < 10:
        pre = cur[-1]*10
        tmp1 = n[i] + chk if n[i] < 9 else 9
        tmp2 = n[i] - chk if chk < n[i] else 0
        base = n[i-1] * 10 + n[i]

        if tmp1 in avail:
            comp1 = pre + save
            comp2 = pre + tmp1
            if abs(base - comp2) < abs(base - comp1):
                save = tmp1

        if tmp2 in avail:
            comp1 = pre + save
            comp2 = pre + tmp2
            if abs(base - comp2) < abs(base - comp1):
                save = tmp2

        chk += 1

    cur.append(save)

print(cur)
cnt = len(cur)
cur = int(''.join(map(str, cur)))
n = int(''.join(map(str, n)))
cnt += abs(n-cur)
cnt = min(abs(n-100), cnt)

print(cnt)