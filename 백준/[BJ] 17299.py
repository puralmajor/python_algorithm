import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
c = Counter(arr)
answer = [-1] * n
stack = []
