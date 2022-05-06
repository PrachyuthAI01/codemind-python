n=int(input())
c=0
r=0
f=0
l=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c==2):
    while(n):
        f=0
        d=n%10
        r+=1
        for x in range(1,d+1):
            if(d%x==0):
                f+=1
        n=n//10
        if(f==2):
            l+=1
    if(r==l):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
        