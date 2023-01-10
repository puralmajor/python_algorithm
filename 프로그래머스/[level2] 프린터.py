from collections import deque


def solutions(priorities, location):
    cur = deque([idx for idx in range(len(priorities))])
    priorities = deque(priorities)
    printed = []
    while priorities:
        if priorities[0] != max(priorities):
            cur.append(cur.popleft())
            priorities.append(cur.popleft())
        else:
            priorities.popleft()
            printed.append(cur.popleft())

    return printed.index(location)+1
