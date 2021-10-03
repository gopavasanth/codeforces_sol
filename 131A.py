#Question: https://codeforces.com/problemset/problem/131/A

l = []
l = input()
if l.isupper():
    print (l.lower())
elif l[1:].isupper():
    print (l[0].upper() + l[1:].lower())
elif len(l) == 1:
    if l.isupper():
        print (l.lower())
    elif l.islower():
         print (l.upper())
else:
    print (l)
    
#instead of many if-else
a=str(input())
if ((a[1:]==a[1:].upper()) and(a[0]==a[0].lower())):
    print (a[0].upper()+a[1:].lower())
elif (a==a.upper()):
    print (a.lower())
else:
    print (a)
