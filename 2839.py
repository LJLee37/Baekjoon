N = int(input())
if N < 3 or N == 4 or N == 7:
    print(-1)
    exit()
f = N // 5
N %= 5
while N % 3 != 0:
    f -= 1
    N += 5
print(f + N//3)

