h, w, n, m = map(int, input().split())
area = h*w
box = (n+1)*(m+1)
print(area//box)