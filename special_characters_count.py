a='abcdefghijklmno pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
s=input()
c=0
for i in s:
    if i not in a:
        c+=1
print(c)