x, y = map(int, input().split())
mo = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if x > 1:
    y += sum(mo[:x - 1])
y %= 7
if y == 0:
    print("SUN")
elif y == 1:
    print("MON")
elif y == 2:
    print("TUE")
elif y == 3:
    print("WED")
elif y == 4:
    print("THU")
elif y == 5:
    print("FRI")
elif y == 6:
    print("SAT")
