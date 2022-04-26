import math
p,r,t=map(int,input().split())
x=pow(1+(r/100),t)
ci=p*x
print("%0.2f"%ci)