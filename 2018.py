N = int(input())
retval = 0
start = 1
end = 1
while end <= N:
    pSum = sum(range(start, end + 1))
    if pSum == N:
        retval += 1
        start += 1
    elif pSum > N:
        start += 1
    else:
        end += 1
print(retval)
