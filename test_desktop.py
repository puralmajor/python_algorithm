from collections import deque


def solution(picks, minerals):
    answer = 0
    energy = []
    charges = {'diamond': 25, 'iron': 5, 'stone': 1}
    minerals = minerals[:sum(picks) * 5]
    for i in range(0, len(minerals), 5):
        energy.append(sum(map(lambda x: charges[x], minerals[i:i + 5])))

    e_sort = sorted(enumerate(energy), key=lambda x: x[1], reverse=True)
    order = [None] * len(e_sort)

    for i in range(len(e_sort)):
        if picks[0]:
            order[e_sort[i][0]] = 'diamond'
            picks[0] -= 1
        elif picks[1]:
            order[e_sort[i][0]] = 'iron'
            picks[1] -= 1
        else:
            order[e_sort[i][0]] = 'stone'
            picks[2] -= 1

    order = deque(order)
    iron = {'diamond': 5, 'iron': 1, 'stone': 1}
    stone = {'diamond': 25, 'iron': 5, 'stone': 1}

    for i in range(0, len(minerals), 5):
        cur = order.popleft()
        if cur == 'diamond':
            answer += len(minerals[i:i+5])
        elif cur == 'iron':
            answer += sum(map(lambda x: iron[x], minerals[i:i + 5]))
        elif cur == 'stone':
            answer += sum(map(lambda x: stone[x], minerals[i:i + 5]))


    return answer

a = [1, 1, 0]
b = ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond"]
print(solution(a, b))