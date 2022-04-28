v=int(input())
pro=1
sum=0
while(v):
    d=v%10
    sum=sum+d
    pro=pro*d
    v=v//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")