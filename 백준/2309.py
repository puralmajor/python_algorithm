import sys
from collections import deque
inp = sys.stdin.readline

heights = []
for _ in range(9):
    heights.append(int(inp()))

heights.sort()
heights = deque(heights)

stack = []
while sum(heights) != 100:
    cur = sum(heights)
    if 100 < cur:
        stack.append(heights.pop())
    elif 100 > cur:
        heights.appendleft(stack.pop(1))


heights = sorted(list(heights))
print(*heights, sep='\n')