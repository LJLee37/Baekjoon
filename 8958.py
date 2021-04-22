n = int(input())
for i in range(n):
    case = input()
    cur = 0
    score = 0
    for i in case:
        if i == 'O':
            cur += 1
            score += cur
        else:
            cur = 0
    print(score)
