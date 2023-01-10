import sys
from itertools import permutations
sdq = []
nums = set([i for i in range(1, 10)])
for _ in range(9):
    sdq.append(list(map(int, sys.stdin.realine().split())))

def dfs(idx):
    if idx == 9:
        return
    temp = nums - set(sdq[idx])
    arr = list(permutations(temp, len(temp)))
    empty = list(filter(lambda x: sdq[idx][x] == 0, range(len(sdq[idx]))))
    t = 0
    for i in empty:
        sdq[i]