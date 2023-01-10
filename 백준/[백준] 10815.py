n = int(input())
# set은 해시로 구현되어 있으므로 list로 탐색하는 것보다 일반적으롤 더 적은 시간이 걸림
sg = set(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

for i in test:
    if i in sg:
        print(1, end=' ')
    else:
        print(0, end=' ')