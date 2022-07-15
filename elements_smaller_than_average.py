n=int(input())
a=list(map(int,input().split()))
d=sum(a)//n
c=0
for i in a:
    if i<=d:
        c+=1
print(c)