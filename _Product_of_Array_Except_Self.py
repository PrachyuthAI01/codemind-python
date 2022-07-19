n=int(input())
a=list(map(int,input().split()))
s=1
d=[]
for i in a:
    s=1
    for j in a:
        s*=j
    d.append(s//i)
print(*d)