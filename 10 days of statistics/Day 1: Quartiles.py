import sys

#One Integer
n = int(input().strip())
#Multiple integers in a line
x = [int(w_temp) for w_temp in input().strip().split(' ')]
x.sort()
#print (x)
q=[0,0,0]
def med(w):
    if len(w) % 2 == 0:
        half=int(len(w)/2)
        median =sum(w[half-1:half+1])/2
    else:
        half=int((len(w)-1)//2)
        median =w[int(len(w)//2)]
    return median,half
q[1],p_median=med(x)
#print (x[:p_median],x[p_median+(n%2):])
q[0],q[2]=med(x[:p_median])[0],med(x[p_median++(n%2):])[0]
for i in q:
    print (int(i))
