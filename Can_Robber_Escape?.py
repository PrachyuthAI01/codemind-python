n=int(input())
c=0
A=list(map(int,input().split()))
for i in A:
    if(i%2!=0):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")