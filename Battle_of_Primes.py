n=int(input())
m=int(input())
s=n+m
t=s
s=s+1
while (s>=0):
    c=0
    for i in range(1,s+1):
        if(s%i==0):
            c+=1
    if(c==2):
        np=s
        break
    s+=1
print(np-t)
        
        
    