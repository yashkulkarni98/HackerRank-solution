#!/bin/python3
import statistics

L = list()
U = list()
S = list()

N = int(input().strip())
X = [int(e) for e in input().split(' ')]
F = [int(e) for e in input().split(' ')]

def freq_append(val, freq):
    for x in range(freq):
        S.append(val)

for i in range(N):
    freq_append(X[i], F[i])

median = statistics.median(S)

for x in S:
    if x < median:
        L.append(x)
    elif x > median:
        U.append(x)

Q1 = statistics.median(L)
Q2 = median
Q3 = statistics.median(U)

print(Q3 - Q1)
