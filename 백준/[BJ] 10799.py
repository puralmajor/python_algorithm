import sys

bars = sys.stdin.readline().rstrip()
bars = bars.replace('()', '|')
bar = []
answer = 0

for i in bars:
    if i == '|':
        answer += len(bar)
    elif i == '(':
        answer += 1
        bar.append(i)
    else:
        bar.pop()

print(answer)
