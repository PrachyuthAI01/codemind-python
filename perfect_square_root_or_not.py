v=int(input())
p=1
i=0
for p in range(v):
    r=p*p
    if(r==v):
        i+=1
if(i==1):
    print("True")
else:
    print("False")