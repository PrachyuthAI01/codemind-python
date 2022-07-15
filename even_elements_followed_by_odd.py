n=int(input())
a=list(map(int,input().split()))
d=[]
s=[]
for i in a:
    if i%2==0:
        d.append(i)
    else:
        s.append(i)
print(*(d+s))
    