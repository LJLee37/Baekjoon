N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
usedCoinCount = 0
coins = list(reversed(coins))
for coin in coins:
    if K >= coin:
        usedCoinCount += K // coin
        K %= coin
print(usedCoinCount)
