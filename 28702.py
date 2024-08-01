FizzBuzzs = [input() for x in range(3)]
isNumberExist = False
lastNumberIndex = -1
for i in range(2, -1, -1):
    if FizzBuzzs[i].isdigit():
        lastNumberIndex = i
        break
lastNumber = int(FizzBuzzs[lastNumberIndex])
targetNumber = lastNumber + 3 - lastNumberIndex
if targetNumber % 3 == 0:
    print("Fizz", end="")
if targetNumber % 5 == 0:
    print("Buzz", end="")
if targetNumber % 3 != 0 and targetNumber % 5 != 0:
    print(targetNumber, end="")
print("")
