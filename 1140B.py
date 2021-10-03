#https://codeforces.com/problemset/problem/1140/B

rep = int(input())

for i in range(rep):
    a = int(input())
    string = input()
    count = 0
    if(string[0] == "<" and string[-1] == ">"):
        for i in range(len(string)):
            if(string[i] == "<" and string[len(string)-1-i] =='>' ):
                count += 1
            else:
                break
    print(count)