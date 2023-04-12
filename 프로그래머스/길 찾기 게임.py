from collections import defaultdict
from collections import defaultdict


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
            parent = (None, 10 ** 7)  # parent, dist
            for nx, x_prime in floor[keys[h + 1]]:
                if abs(x_ - x_prime) < parent[1]:
                    parent = (nx, abs(x_ - x_prime))

            if x_ < x_prime:
                tree[parent[0]][0] = node
            else:
                tree[parent[0]][1] = node

    root = floor[keys[-1]][0][0]
    pre = []
    post = []
    for i in range(1, len(tree)):
        print(i, tree[i])
    preorder(root)
    postorder(root)
    return [pre, post]

ni = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(ni))