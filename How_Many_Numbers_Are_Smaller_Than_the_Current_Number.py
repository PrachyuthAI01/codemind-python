n=int(input())
a=list(map(int,input().split()))
c=0
d=[]
for i in a:
    c=0
    for j in a:
        if i>j:
            c+=1
    d.append(c)
print(*d)