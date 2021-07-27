N, X = map(int, input().split())
A = list(map(int, input().split()))
smaller = [x for x in A if x < X]
for i in smaller:
    print(i, end=' ')
