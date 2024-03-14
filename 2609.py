a, b = [int(x) for x in input().split()]
maximumCommonSubstructure = 1
for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        maximumCommonSubstructure = i
print(maximumCommonSubstructure)
leastCommonMultiple = (a * b) // maximumCommonSubstructure
print(leastCommonMultiple)