n = int(input())
l=[]
count=0
l=list(map (int, input().split()))
#print (l)
sum = sum(l)
#print (sum)
sum2 = 0
for i in range(0,n-1):
    sum2 = sum2 + l[i]
    count = count + (l[i] * (sum - sum2)) 
print (count)
