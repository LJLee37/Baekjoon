a1, a0 = [int(i) for i in input().split()]
c = int(input())
n0 = int(input())
if c is a1:
    if a0 >= 0:
        print(1)
    else:
        print(0)
elif c > a1:
    print(0)
else:
    if a1*n0 + a0 >= c*n0:
        print(1)
    else:
        print(0)