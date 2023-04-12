s = int(input())
stack = 0
cur = 1
time = 0

while 2*cur <= s:
    time += 2
    cur *= 2

stack = cur//2
