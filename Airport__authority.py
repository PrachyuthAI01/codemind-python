n=int(input())
a=[]
c=0
for i in range(0,n):
    d=int(input())
    a.append(d)
s=int(input())
for j in a:
    if j<=s:
        c+=1
    elif j>s:
        c+=2
print(c)
    