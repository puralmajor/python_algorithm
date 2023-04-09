a = 0.1312412415125432524134235
b = 0.2374134123526354752347124
c = 0.12
d = 0.2735683265869812748968936
arr = [a,b,c,d]
answer = 0

for i in arr:
    temp = round(i*100, 3)
    answer += temp
    print('{:.3f}'.format(answer))
