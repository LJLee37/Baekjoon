N, M = map(int, input().split())
board = []
for i in range(N):
    temp = []
    inp = input()
    for j in inp:
        if j == 'W':
            temp.append(True)
        else:
            temp.append(False)
    board.append(temp)
change_needed = []
for i in range(N - 8):
    temp = []

