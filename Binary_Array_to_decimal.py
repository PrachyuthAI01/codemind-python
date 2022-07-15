n=int(input())
a=list(map(int,input().split()))
s=''
for i in a:
    s+=str(i)
dec=0
i=0
s=int(s)
while(int(s)):
    d=s%10
    dec=dec+d*pow(2,i)
    s=s//10
    i+=1
print(dec)
    