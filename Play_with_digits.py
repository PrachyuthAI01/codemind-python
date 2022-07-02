n=int(input())
a=list(map(int,input().split()))
su=0
for i in a:
    s=0
    while(i):
        d=i%10
        s+=d
        i=i//10
    su+=s
print(su)