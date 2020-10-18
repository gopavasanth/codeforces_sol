#Question: https://codeforces.com/problemset/problem/200/B
    
from decimal import *
getcontext().prec=12
n = int(input())
l=list(map(int, input().split()))
#print(l)
sum = 0
for i in range(len(l)):
    sum = sum + (l[i]/100)
a=((sum/n)*100)
print(a)
