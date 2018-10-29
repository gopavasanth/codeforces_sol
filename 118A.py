#This takes input
word = input()
word = word.lower()
l = []
#this is for loop 
for i in range (len(word)):
    if i == 'a' or i=='e' or i == 'i' or i == 'o' or i == 'u' or i=='y' :
        True
    else:
        l.append('.'+word[i])
print("".join(l))        
