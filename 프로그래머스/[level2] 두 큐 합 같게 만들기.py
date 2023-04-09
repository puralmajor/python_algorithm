from collections import deque


def solution(queue1, queue2):
    cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sq1, sq2 = sum(q1), sum(q2)
    half = (sq1 + sq2) // 2

    first_q1 = q1.copy()
    first_q2 = q2.copy()

    while sq1 != sq2:
        before = [sq1, sq2]
        if sq1 < half:
            tmp = q2.popleft()
            q1.append(tmp)
            sq1 += tmp
            sq2 -= tmp
            cnt += 1
        elif sq2 < half:
            tmp = q1.popleft()
            q2.append(tmp)
            sq1 -= tmp
            sq2 += tmp
            cnt += 1
        else:
            break

        print(before)
        print([sq2, sq1])
        print(cnt)

        if before == [sq2, sq1]:
            return -1

        if cnt != 0 and (q1 == first_q1 or q1 == first_q2):
            return -1

        if cnt > 30:
            break
    #        if 4*n < cnt:
    #            return -1

    return cnt


a1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
a2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(a1, a2))