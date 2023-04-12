from collections import deque

n, k = map(int, input().split())

if k == n:
    print(0)
    print(n)
    exit()

elif k < n:
    print(n-k)
    print(*[i for i in range(n, k-1, -1)])
    exit()

visit = set()
q = deque()
q.append((n, [n]))

move = [lambda x: x+1, lambda x: x-1, lambda x: 2*x]

while True:
    cur, path = q.popleft()

    if cur == k:
        print(len(path)-1)
        print(*path)
        break

    visit.add(cur)

    for i in range(3):
        nx = move[i](cur)
        if 0 <= nx <= 200000 and nx not in visit:
            temp = path.copy()
            temp.append(nx)
            q.append((nx, temp))
