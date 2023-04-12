import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 4)


def solution(nodeinfo):
    floor = defaultdict(list)

    def preorder(node):
        if node:
            pre.append(node)
            preorder(tree[node][0])
            preorder(tree[node][1])

    def postorder(node):
        if node:
            postorder(tree[node][0])
            postorder(tree[node][1])
            post.append(node)

    for idx, val in enumerate(nodeinfo):
        idx += 1
        x, y = val
        floor[y].append((idx, x))

    tree = [[None, None] for _ in range(len(nodeinfo) + 1)]
    keys = sorted(floor.keys())

    for h in range(len(keys) - 1):
        for node, x_ in floor[keys[h]]:
            if node == 1:
                print(node, x_)
            parent = (None, 10 ** 7)  # parent, dist
            for nx, x_prime in floor[keys[h + 1]]:
                if abs(x_ - x_prime) < parent[1]:
                    parent = (nx, abs(x_ - x_prime))
            if node == 1:
                print(parent)
            if x_ < x_prime:
                tree[parent[0]][0] = node
            else:
                tree[parent[0]][1] = node

    print(*tree)
    root = floor[keys[-1]][0][0]
    pre = []
    post = []
    preorder(root)
    postorder(root)
    return [pre, post]


ni = [[1, 1], [3, 2], [4, 1], [5, 3], [6, 4], [7, 2], [8, 1], [9, 3], [10, 2], [11, 1]]
print(solution(ni))