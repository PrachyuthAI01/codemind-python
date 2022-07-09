n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
for i in a:
    if i in b:
        continue
    else:
        d.append(i)
for i in b:
    if i in a:
        continue
    else:
        d.append(i)
print(*d)