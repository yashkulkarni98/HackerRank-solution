from __future__ import division

def get_median(a):
    #print a
    n = len(a)
    median = a[n//2]
    #print median
    if n%2 == 0:
        #print a[n/2-1:n/2]
        median = sum(a[n//2-1:n//2+1])/2
    return median
        
n = int(raw_input())
a = map(int, raw_input().split())
freq = map(int, raw_input().split())
array = []
for i in range(n):
    array.extend([a[i] for x in range(freq[i])])
array.sort()
n = len(array)
#print array, n
median = get_median(array)
l = [x for x in array[0:n//2] if x < median]
r = [x for x in array[n//2+1:n] if x > median]
if n % 2 == 0:
    l = [x for x in array[0:n//2] if x < median]
    r = [x for x in array[n//2:n] if x > median]

#print l, get_median(l)
#print r, get_median(r)
print round(get_median(r) - get_median(l), 1)
