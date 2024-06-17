N, M = [int(x) for x in input().split()]
cards = [int(x) for x in input().split() if int(x) < M]
cards.sort(reverse=True)
candidate = 0
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            sum = cards[i] + cards[j] + cards[k]
            if sum > candidate and sum <= M:
                candidate = sum
print(candidate)
