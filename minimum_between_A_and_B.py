n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
d=[]
for i in a:
    if i<=l and i>=k:
        d.append(i)
if len(d)!=0:
    print(min(d))
else:
    print('-1')
        