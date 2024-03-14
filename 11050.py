factorials = [1, 1]
N, K = [int(x) for x in input().split()]
if K < 0 or K > N:
    print(0)
    exit()
for i in range(2, N + 1):
    factorials.append(factorials[-1] * i)
print(factorials[N] // (factorials[K] * factorials[N - K]))
