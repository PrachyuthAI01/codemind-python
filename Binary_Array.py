n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==1 or i==0:
        c+=1
    else:
        print(False)
        break
if c==n:
    print(True)
        
