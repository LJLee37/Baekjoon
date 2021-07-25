numbers = [int(input()) for _ in range(9)]
maxNumber = max(numbers)
maxIndex = numbers.index(maxNumber)
print(maxNumber)
print(maxIndex+1)
