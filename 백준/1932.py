import sys
input = sys.stdin.readline

n = int(input())
tree = []

for i in range(n):
    inp = list(map(int, input().split()))
    if i == 0:
        tree.append(inp)
        continue
    elif i == 1:
        tree.append(list(map(lambda x: x+tree[0][0], inp)))
        continue

    inp[0] += tree[-1][0]
    inp[-1] += tree[-1][-1]

    for j in range(1, len(inp)-1):
        inp[j] += max(tree[-1][j-1], tree[-1][j])

    tree.append(inp)

print(max(tree[-1]))


