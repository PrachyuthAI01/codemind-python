n=int(input())
a=list(map(int,input().split()))
s=0
d=0
for i in a:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        s+=i
        d+=1
print('%0.2f'%(s/d))