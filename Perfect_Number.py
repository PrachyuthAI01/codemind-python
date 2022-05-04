p=int(input())
sum=0
for i in range(1,p):
    if(p%i==0):
        sum=sum+i
if(sum==p):
    print(True)
else:
    print(False)