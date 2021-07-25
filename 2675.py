T = int(input())
for _ in range(T):
    N, S = input().split()
    N = int(N)
    for i in S:
        print(i * N, end='')
    print()
