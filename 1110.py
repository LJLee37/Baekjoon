N = int(input())
N = (N // 10, N % 10)
count = 1
if len(N) == 1:
    N = (0, N[0])
n = (N[1], (N[0] + N[1]) % 10)
while n != N:
    n = (n[1], (n[0] + n[1]) % 10)
    count += 1
print(count)
