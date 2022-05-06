n=int(input())
li=list(map(int,input().split()))
num=''
for i in li:
    num+=str(i)
num=int(num)+1
a=list(str(num))
print(*a)