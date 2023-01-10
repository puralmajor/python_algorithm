from collections import deque


def check(s):
    s = deque(s)
    stack = []
    flag = True
    while s:
        cur = s.popleft()
        if not stack:
            if cur == ')':
                flag = False
                break
            else:
                stack.append(cur)
                continue

        if stack:
            if cur == '(':
                stack.append(cur)
            else:
                stack.pop()

    if len(stack) != 0:
        flag = False

    return flag


def change(s):
    if not s:
        return ''

    u, v = '', ''
    for i in range(len(s)):
        if s[:i+1].count('(') != 0 and s[:i+1].count('(') == s[:i+1].count(')'):
            u = s[:i+1]
            v = s[i+1:]
            break

    print(u, v)
    if check(u):
        u = u + change(v)
    else:
        tmp = '('
        tmp += change(v)
        tmp += ')'
        u = u[1:-1]
        u = u.replace('(', ']')
        u = u.replace(')', '[')
        u = u.replace(']', ')')
        u = u.replace('[', '(')
        u = tmp + u

    return u


def solution(p):
    if check(p):
        return p
    else:
        return change(p)


x = "()))((()"
print(solution(x))