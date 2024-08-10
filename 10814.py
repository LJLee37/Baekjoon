N = int(input())
members = []
for i in range(N):
    rawInput = input().split()
    members.append((int(rawInput[0]), rawInput[1], i))
members.sort(key=lambda x: (x[0], x[2]))
for member in members:
    print(member[0], member[1])
