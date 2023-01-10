from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque()
    gone = []
    time = deque()

    while truck_weights:
        answer += 1
        while time and answer - time[0] >= bridge_length:
            time.popleft()
            gone.append(bridge.popleft())

        if not bridge:
            bridge.append(truck_weights.popleft())
            time.append(answer)
            continue

        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
            time.append(answer)

    while bridge:
        answer += 1
        while time and answer - time[0] >= bridge_length:
            time.popleft()
            gone.append(bridge.popleft())

    return answer


print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
