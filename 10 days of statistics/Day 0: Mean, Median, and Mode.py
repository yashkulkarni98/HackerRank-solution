# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = list(map(int, input().split()))
print(round(sum(a)/n, 1))
a.sort()
if(n%2 == 1):
    print(round(a[n//2], 1))
else:
    print(round((a[(n-1)//2]+a[(n+1)//2])/2, 1))
count = dict()
for i in a:
    count[i] = 0
for i in a:
    count[i] += 1
large = count[a[0]]
key = a[0]
for i in count:
    if(large < count[i]):
        large = count[i]
        key = i
    elif(large == count[i]):
        if(key > i):
            large = count[i]
            key = i
print(key)
