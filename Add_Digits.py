n=int(input())
t=n
s=0
while(n):
    d=n%10
    s+=d
    n=n//10
    if(n==0 and s>9):
        n=s
        s=0
if(s>0 and s<10):
    print(s)