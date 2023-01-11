from collections import deque

a, b = map(int,input().split())
m = int(input())
nums = list(map(int, input().split()))
dec = 0
new_nums = deque()
for i in range(m):
    dec += a**(m-i-1) * nums[i]



while dec:
    new_nums.appendleft(dec%b)
    dec = dec//b

print(*new_nums)