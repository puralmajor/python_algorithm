import sys
from collections import defaultdict
inp = sys.stdin.readline


def preorder(cur):
    print(cur, end='')
    for i in tree[cur]:
        if i == '.':
            continue
        preorder(i)


def inorder(cur):
    if tree[cur][0] == '.':
        return
    inorder(tree[cur][0])
    print(cur, end='')
    inorder(tree[cur][1])


def postorder(cur):
    for i in tree[cur]:
        if i == '.':
            continue
        postorder(i)
    print(cur, end='')


n = int(inp())
tree = defaultdict(list)

for _ in range(n):
    parent, left, right = inp().split()
    tree[parent] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')