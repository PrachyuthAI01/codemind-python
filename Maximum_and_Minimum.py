n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if a.count(i)==i and i not in d:
        d.append(i)
if len(d)==0:
    print(-1)
else:
    print(min(d),max(d))
