n=int(input())
a=list(map(int,input().split()))
for i in range(1,max(a)+1):
    l=0
    for j in range(len(a)):#21
        if(a[j]%i==0):
            l+=1
    if(l==len(a)):
        v=i
print(v)
            
    
        
    