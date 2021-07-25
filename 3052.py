numbers = [int(input()) for _ in range(10)]

# check how many remainders are when divided by 42


def countRemainders(arr):
    remainders = []
    for num in arr:
        remainder = num % 42
        if remainder not in remainders:
            remainders.append(remainder)
    return len(remainders)


print(countRemainders(numbers))
