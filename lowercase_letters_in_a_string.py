n=input()
a='abcdefghijklmnopqrstuvwxyz'
c=0
for i in n:
    if i in a:
        c+=1
    else:
        continue
print(c)