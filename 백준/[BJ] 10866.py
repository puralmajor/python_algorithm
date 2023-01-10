from collections import deque

dq = deque()
N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == 'push_front':
        dq.appendleft(command[1])

    elif command[0] == 'push_back':
        dq.append(command[1])

    elif command[0] == 'pop_front':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())

    elif command[0] == 'pop_back':
        if not dq:
            print(-1)
        else:
            print(dq.pop())

    elif command[0] == 'size':
        print(len(dq))

    elif command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])

    elif command[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])