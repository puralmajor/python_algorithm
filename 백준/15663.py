from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in sorted(list(set(permutations(arr, m)))):
    print(*i)