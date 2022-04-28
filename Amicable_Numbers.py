v=int(input())
p=int(input())
t=v
x=p
d=0
r=0
for i in range(1,v):
    if(v%i==0):
        r=r+i
for f in range(1,p):
    if(p%f==0):
        d=d+f
if(d==t and r==x):
    print("Amicable")
else:
    print("Not Amicable")