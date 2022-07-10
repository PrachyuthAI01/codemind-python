n=input()
a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
c=0
for i in n:
    if i in a:
        continue
    else:
        c+=1
print(c)
