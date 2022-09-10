n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if i==a.count(i) and i not in d:
        d.append(i)
if len(d)!=0:
    print(*d)
else:
    print('-1')
        