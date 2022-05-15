v=input()
for i in range(0,len(v)):
    x=0
    for j in range(0,len(v)):
        if(v[i]==v[j] and j!=i):
            x-=1
    if(x==0):
        print(i)
        break
else:
    print('-1')