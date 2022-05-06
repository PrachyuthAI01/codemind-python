n=int(input())
a=list(map(int,input().split()))
p=int(input())
dic=dict()
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
li=[]
for i in dic:
    if(p==dic[i]):
        li.append(i)
if(li==[]):
    print(-1)
else:
    print(*li)