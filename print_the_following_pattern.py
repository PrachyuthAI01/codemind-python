n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==n-1 or i==j or j==0):
            print('*',end='')
        else:
            print(end=' ')
    print()