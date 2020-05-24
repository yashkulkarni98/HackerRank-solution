import math


n=int(input())
arr=list(map(int,input().strip().split()))
u=int(sum(arr)/n)
sum=0
for value in arr:
    sum+=((value-u)**2)
print(round(math.sqrt(sum/n),1))
