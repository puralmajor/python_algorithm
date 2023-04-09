from collections import deque

n, k = map(int, input().split())

q = deque()
q.append((n, 0))
visit = set()
move = [lambda x: x+1, lambda x: x-1, lambda x: 2*x]

while True:
    cur, v = q.popleft()
    if cur == k:
        print(v)
        break

    visit.add(cur)

    for i in range(3):
      nx = move[i](cur)
      if 0 <= nx <= 200000 and nx not in visit:
        q.append((nx, v+1))