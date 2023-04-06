from collections import deque

n, k = map(int, input().split())

if k == n:
    print(0)
    print(n)
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
        if 0 <= nx <= 100000 and nx not in visit:
            path.append(nx)
            q.append(nx)
            path.pop()
