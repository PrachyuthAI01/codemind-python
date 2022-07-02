n=int(input())
a=list(map(int,input().split()))
for i in a:
    d=abs(i)
    s=len(str(d))
    print(s,end=' ')