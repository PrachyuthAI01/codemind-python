s=str(input())
v1='aeiou'
v2='AEIOU'
c1=0
c2=0
for i in v1:
    if i in s:
        c1+=1
for i in v2:
    if i in s:
        c2+=1
if c1==5 or c2==5:
    print(True)
else:
    print(False)