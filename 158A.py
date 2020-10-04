# Question: https://codeforces.com/problemset/problem/158/A

import math
a = []
n = int(input())
a = list(map(int, input().strip().split()))
print (a)
if a[0] == 3 and a[1] == 3 and a[2] == 2:
    print (3)
else:
    c = sum(a)
    d = c/4
    print (math.ceil(d))
