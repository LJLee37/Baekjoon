N, M = map(int, input().split())
A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)
M, K = map(int, input().split())
B = []
for i in range(M):
    temp = list(map(int, input().split()))
    B.append(temp)
for i in range(N):
    for j in range(K):
        num = 0
        for k in range(M):
            num += A[i][k]*B[k][j]
        print(num, end=' ')
    print("")

