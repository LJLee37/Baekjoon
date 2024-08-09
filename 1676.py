twos = 0
fives = 0
N = int(input())
for i in range(1, N + 1):
    tempTwo = i
    while tempTwo % 2 == 0:
        twos += 1
        tempTwo //= 2
    tempFive = i
    while tempFive % 5 == 0:
        fives += 1
        tempFive //= 5
print(min(twos, fives))
