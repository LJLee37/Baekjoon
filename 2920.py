sounds = [int(x) for x in input().split()]


def isAscending(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True


def isDescending(s):
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            return False
    return True


if isAscending(sounds):
    print("ascending")
elif isDescending(sounds):
    print("descending")
else:
    print("mixed")
