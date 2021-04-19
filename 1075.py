N = int(input())
F = int(input())
N = N // 100 * 100
answer = F - N % F
if answer == F:
    answer = 0
if answer < 10:
    print(0,end='')
print(answer)
