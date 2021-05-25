N = int(input())
li = list(map(int, input().split()))
li.sort()
def binsearch(low, high, target):
    mid = (low + high) // 2
    if li[mid] == target:
        return 1
    elif low == high or high - low < 2:
        if li[high] == target:
            return 1
        return 0
    elif li[mid] > target:
        return binsearch(low, mid, target)
    else:
        return binsearch(mid, high, target)

M = int(input())
t = list(map(int, input().split()))
for i in t:
    print(binsearch(0, N - 1, i))
