def isvowel(i):
    a='aeiouAEIOU'
    if i in a:
        return 1
    else:
        return 0
n=input()
c=0
for i in n:
    if(isvowel(i)):
        c+=1
print(c)
        