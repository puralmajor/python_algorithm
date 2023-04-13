from collections import deque


def solution(picks, minerals):
    answer = 0
    energy = []
    charges = {'diamond': 3, 'iron': 2, 'stone': 1}
    for i in range(0, len(minerals), 5):
        energy.append(sum(map(lambda x: charges[x], minerals[i:i + 5])))

    e_sort = sorted(energy, reverse=True)
    order = dict()

    for i in range(len(energy)):
        if order.get(e_sort[i]):
            if picks[0]:
                order[e_sort[i]][0] += 1
                picks[0] -= 1
            elif picks[1]:
                order[e_sort[i]][1] += 1
                picks[1] -= 1
            elif picks[2]:
                order[e_sort[i]][2] += 1
                picks[2] -= 1
            else:
                break
        else:
            if picks[0]:
                order[e_sort[i]] = [1, 0, 0]
                picks[0] -= 1
            elif picks[1]:
                order[e_sort[i]] = [0, 1, 0]
                picks[1] -= 1
            elif picks[2]:
                order[e_sort[i]] = [0, 0, 1]
                picks[2] -= 1
            else:
                break

    pixes = deque()
    for i in range(len(energy)):
        if order.get(energy[i]):
            using = order[energy[i]]
            if using[0]:
                pixes.append('diamond')
                using[0] -= 1
            elif using[1]:
                pixes.append('iron')
                using[1] -= 1
            elif using[2]:
                pixes.append('stone')
                using[2] -= 1

            order[energy[i]] = using
            if sum(order[energy[i]]) == 0:
                del order[energy[i]]
        else:
            pixes.append(-1)

    iron = {'diamond': 5, 'iron': 1, 'stone': 1}
    stone = {'diamond': 25, 'iron': 5, 'stone': 1}

    for i in range(0, len(minerals), 5):
        cur = pixes.popleft()
        if cur == -1:
            break
        elif cur == 'diamond':
            answer += 5
        elif cur == 'iron':
            answer += sum(map(lambda x: iron[x], minerals[i:i + 5]))
        elif cur == 'stone':
            answer += sum(map(lambda x: stone[x], minerals[i:i + 5]))

    return answer