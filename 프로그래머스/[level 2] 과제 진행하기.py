from collections import deque


def solution(plans):
    answer = []
    plans = map(lambda x: (x[0], list(map(int, x[1].split(':'))), int(x[2])), plans)
    plans = deque(sorted(plans, key=lambda x: (x[1], x[2])))
    stack = []
    time = plans[0][1]

    while True:
        if not plans and not stack:
            break

        if plans and time >= plans[0][1]:
            subject, start, spend_m = plans.popleft()
        elif stack:
            subject, spend_m = stack.pop()

        end_time = [time[0], time[1] + spend_m]
        if end_time[1] >= 60:
            end_time[0] += end_time[1] // 60
            end_time[1] = end_time[1] % 60

        if plans and end_time > plans[0][1]:
            diff = (plans[0][1][0] - time[0]) * 60 + (plans[0][1][1] - time[1])
            time = plans[0][1]
            stack.append((subject, spend_m - diff))
        else:
            answer.append(subject)
            if stack:
                time = max(end_time, stack[-1][1])

    return answer