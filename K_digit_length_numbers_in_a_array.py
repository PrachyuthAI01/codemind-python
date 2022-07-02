n,t=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    i=abs(i)
    s=str(i)
    if(len(s)==t):
        c+=1
print(c)