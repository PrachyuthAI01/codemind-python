n=int(input())
a=list(map(int,input().split()))
x=0
for i in a:
    c=0
    while(i):
        d=i%10
        c+=1
        i=i//10
    if c%2==0:
        x+=1
print(x)