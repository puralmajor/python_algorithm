class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.post = None

class LinkedList:
    def __init__(self):
        self.n = 0
        self.head = None
        self.cur = None

def solution(n, k, cmd):
    mylist = LinkedList()

    for i in range(n):
        node = Node(i)
        if i == 0:
            mylist.head = node
            mylist.cur = node
        else:
            mylist.cur.post = node
            node.pre = mylist.cur
            mylist.cur = node

        if i == k:
            cur = node

    mylist.cur = cur
    deleted = []

    for command in cmd:
        c = command.split()
        if len(c) == 2:
            c, idx = c[0], int(c[1])
        else:
            c = c[0]

        if c == 'U':
            while idx and cur.pre:
                cur = cur.pre
                idx -= 1

            mylist.cur = cur

        if c == 'D':
            while idx and cur.post:
                cur = cur.post
                idx -= 1

            mylist.cur = cur

        if c == 'C':
            if cur.post:
                if cur.pre:
                    cur.post.pre, cur.pre.post = cur.pre, cur.post
                else:
                    cur.post.pre = None
                deleted.append(cur)
                cur = cur.post
            else:
                cur.pre.post = None
                deleted.append(cur)
                cur = cur.pre

            mylist.cur = cur

        if c == 'Z':
            if len(deleted) != 0:
                restore = deleted.pop()
                if restore.pre:
                    restore.pre.post = restore
                if restore.post:
                    restore.post.pre = restore

    answer = ['O'] * n
    for i in deleted:
        answer[i.val] = 'X'

    return ''.join(answer)


cmd = ["C"]
print(solution(8, 0, cmd))