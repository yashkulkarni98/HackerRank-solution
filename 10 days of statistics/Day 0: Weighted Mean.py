N = int(input())
Arr = input().split(" ")
Weights = input().split(" ")
Wmean=0
SumWt=0
for i in range(0, N):
    Wmean+=(int(Arr[i])*int(Weights[i]))
    SumWt += int(Weights[i])
Wmean = Wmean/SumWt
print(round(Wmean, 1))
