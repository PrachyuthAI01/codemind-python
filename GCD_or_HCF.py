p,v=map(int,input().split())
if(p>v):
    for i in range(1,p):
        if(p%i==0 and v%i==0):
            gcd=i
else:
    for i in range(1,v):
        if(p%i==0 and v%i==0):
            gcd=i
print(gcd)