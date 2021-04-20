apt = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
T = int(input())
row = 1
for i in range(T):
    k = int(input())
    n = int(input())
    if row <= k:
        for i in range(row, k + 2):
            temp = []
            for j in range(14):
                temp.append(sum(apt[row-1][:j + 1]))
            apt.append(temp)
            row += 1
    print(apt[k][n - 1])

