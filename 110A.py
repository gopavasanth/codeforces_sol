#Question: https://codeforces.com/problemset/problem/110/A 

num = input()
count = 0
for i in range(len(num)):
    if (num[i]) == '4' or (num[i]) == '7':
        count = count+1       
if count == 7 or count == 4  :
    print("YES")
else:
    print("NO")
