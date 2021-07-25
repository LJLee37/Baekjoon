N = int(input())
A = list(map(int, input().split()))
maxValue = max(A)
for i in range(N):
    A[i] = A[i] * 100 / maxValue
avg = sum(A) / N
print(avg)
