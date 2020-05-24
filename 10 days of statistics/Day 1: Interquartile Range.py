def median(l):
    n = len(l)
    mid = n // 2
    if n % 2 == 0:
        return sum(l[mid-1:mid+1]) / 2
    else:
        return l[mid]

def quartiles(data):
    n = len(data)
    mid = n // 2
    return [float(median(q)) for q in [data[0:mid], data, data[mid+(n%2):]]]
    
n = int(input())
X = [int(x) for x in input().split(" ")]
F = [int(f) for f in input().split(" ")]

S = []
for i,n in enumerate(X):
    S += F[i] * [n]

q = quartiles(sorted(S))
print(q[2] - q[0])
