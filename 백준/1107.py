target = list(input())
m = int(input())
if m == 0:
    print(len(target))
    exit()
broken = set(map(int,input().split()))
answer = 0

avail = set(range(10))
if m:
    avail -= broken
if not avail:
    print(abs(int(''.join(target)) - 100))
    exit()
cur = []

if target == str(100):
    print(0)
    exit()

idx = 0

while idx < len(target) and int(target[idx]) in avail:
    cur.append(target[idx])
    idx += 1

if cur == target:
    print(len(target))
    exit()


lower, upper = cur.copy(), cur.copy()

if not cur:
    low, up = [str(i) for i in avail if i < int(target[0])], [str(i) for i in avail if i > int(target[0])]
    lower, upper = [max(low) if low else min(up)], [min(up) if up else max(low)]

while len(lower) < len(target):
    lower.append(str(max(avail)))

while len(upper) < len(target):
    upper.append(str(min(avail)))

lower = list(map(str, lower))
upper = list(map(str, upper))
lower = int(''.join(lower))
upper = int(''.join(upper))
answer = len(target) if lower != 0 and upper != 0 else 1
target = int(''.join(target))
answer = min(answer+abs(target-lower), answer+abs(upper-target), abs(target-100))
print(answer)