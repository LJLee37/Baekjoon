A = int(input())
B = int(input())
C = int(input())
m = A*B*C
counts = [0]*10
for i in str(m):
    counts[int(i)] += 1
for i in counts:
    print(i)
