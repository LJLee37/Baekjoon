N = int(input())
numbers = {}
for i in [int(x) for x in input().split()]:
    if i not in numbers:
        numbers[i] = 0
    numbers[i] += 1
M = int(input())
for i in [int(x) for x in input().split()]:
    print(numbers[i] if i in numbers else 0, end=" ")
