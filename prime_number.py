v=int(input())
c=0
i=1
for i in range(1,v+1):
    if(v%i==0):
        c+=1
if(c==2):
    print("prime")
else:
    print("not a prime")