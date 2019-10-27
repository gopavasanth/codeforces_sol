a=list(map(int,input().split()))
t=a[0]
d=a[1]
b=list(map(int,input().split()))
count=0
for i in range(t-1):
    if(b[i+1]-b[i]==2*d):
        count+=1
    elif(b[i+1]-b[i]>2*d):
        count+=2
print(count+2)
