n=int(input())
a=n
f=1
s=0
while(n):
    d=n%10
    f=1
    for i in range(1,d+1):
        f*=i
    s=s+f
    n=n//10
if(a==s):
    print('The number',a,'is a strong number')
else:
    print('The number',a,'is not a strong number')