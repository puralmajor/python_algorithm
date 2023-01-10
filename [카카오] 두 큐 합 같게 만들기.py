from collections import deque
def solution(queue1, queue2):
    answer = -1
    target = sum(queue1+queue2) // 2
    q1, q2 = deque(queue1), deque(queue2)
    i, j = 0, 0
    l = len(q1)
    while i < 2*l and j < 2*l and sum(q1) != sum(q2):
        if sum(queue1) < target:
            q1.append(q2.pop())
            i += 1
        else:
            q2.append(q1.pop())
            j += 1

    if sum(q1) == target:
        answer = i+j

    return answer

solution([3,2,7,2], [4,6,5,1])