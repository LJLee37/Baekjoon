N = int(input())
for i in range(N + 1):
    cur = i
    answer = i
    while i > 0:
        cur += i % 10
        i //= 10
    if cur == N:
        print(answer)
        exit(0)
print(0)
