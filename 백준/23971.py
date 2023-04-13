import math
h, w, n, m = map(int, input().split())
h = math.ceil(h/(n+1))
w = math.ceil(w/(m+1))
print(h*w)