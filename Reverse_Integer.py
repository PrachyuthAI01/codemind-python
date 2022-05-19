v=int(input())
t=v
v=abs(v)
s=0
while(v):
    d=v%10
    s=s*10+d
    v=v//10
if(t>0):
    print(s)
else:
    print(-s)
    