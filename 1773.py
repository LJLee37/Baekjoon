N, C = map(int, input().split())
students = []
for i in range(N):
    students.append(int(input()))
answer = 0
for i in range(1, C + 1):
    isDivisible = False
    for j in students:
        if i % j == 0:
            isDivisible = True
            break
    if isDivisible:
        answer += 1
print(answer)
