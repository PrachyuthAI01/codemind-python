n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    c=0
    for x in range(1,i+1):
        if(i%x==0):
            c+=1
    if(c==2):
        print(i)