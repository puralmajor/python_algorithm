n = int(input())
stock = list(map(int, input().split()))
stock.sort()
m = int(input())
req = list(map(int, input().split()))

answer = []

for r in req:
    left, right = 0, n-1
    target = len(answer)
    while left < right:
        mid = (left+right)//2

        if stock[mid] == r:
            answer.append('yes')
            break

        elif stock[mid] < r:
            left = mid+1

        else:
            right = mid-1

    if target == len(answer):
        answer.append('no')

print(*answer)