from collections import deque
import sys

n = int(sys.stdin.readline().strip())
queue = deque()
for _ in range(n):
    command = list(sys.stdin.readline().split())
    com = command[0]
    if com == 'push':
        queue.append(command[1])

    if com == 'pop':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue.popleft())

    if com == 'size':
        print(len(queue))

    if com == 'empty':
        print(1) if len(queue) == 0 else print(0)

    if com == 'front':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])

    if com == 'back':
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[-1])
