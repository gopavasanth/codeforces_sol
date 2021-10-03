import math
n = int(input())
#a = n%5
#a=a/2
while n>5:         
    n=n-5
    n=n/2
    #a=n
a=math.ceil(n)
if a == 1:
    print("Sheldon")
elif a==2:
    print("Leonard")
elif a==3:
    print("Penny")    
elif a==4:
    print("Rajesh")
elif a==5:
    print("Howard")

