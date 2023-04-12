from queue import PriorityQueue


def solution(n, k, enemy):
    answer = 0
    end = len(enemy)
    if k == end:
        return end

    deleted = PriorityQueue()
    for e in enemy:
        n -= e
        deleted.put(-e)
        if n < 0:
            if k == 0:
                return answer
            else:
                n -= deleted.get()
                k -= 1
        answer += 1

    return end


print(solution(100, 1, [1,1,1,1,1,1,1,1,1,1,1,100,1,100,1,1,1,1,1]))