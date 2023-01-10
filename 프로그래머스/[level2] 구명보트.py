def solution(people, limit):
    stack_people = sorted(people)
    cnt = 0

    while stack_people:
        if max(stack_people) + min(stack_people) > limit:
            cnt += 1
            stack_people.pop()
            continue
