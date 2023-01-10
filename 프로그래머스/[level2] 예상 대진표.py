from collections import deque


def solution(n, a, b):
    answer = 0
    contest = [i+1 for i in range(n)]
    a, b = min(a, b), max(a, b)
    after = []

    for x in range(a, -1, 2):
        after.append(x)

    return after

# def solution(n,a,b):
#     answer = 0
#     p = [i+1 for i in range(n)]
#     c, d = min(a,b), max(a,b)
#     # 작은 쪽은 작은 쪽의 홀/짝에 따라 승리, 그 이상은 큰 쪽 따라 승리
#     while True:
#         answer += 1
#         x, y = p.index(c)+1, p.index(d)+1
#         if x % 2 == 0:
#             if y % 2 != 0:
#                 p = p[1:x:2] + p[x::2]
#             else:
#                 p = p[1:x:2] + p[x+1::2]
#         else:
#             if y % 2 != 0:
#                 p = p[:x:2] + p[x+1::2]
#             else:
#                 p = p[:x:2] + p[x+2::2]

#         print(p)
#         if answer == 10:
#             break
#     return answer
