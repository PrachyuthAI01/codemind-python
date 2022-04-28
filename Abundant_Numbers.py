v=int(input())
sum=0
for i in range(1,v):
    if(v%i==0):
        sum=sum+i
if(sum>v):
    print("True")
else:
    print(False)