def bottomUp(n):
    li = [i - 1 for i in range(n + 1)]
    for i in range(n + 1):
        if i < n:
            li[i + 1] = min(li[i] + 1, li[i + 1])
        if i * 2 <= n:
            li[i * 2] = min(li[i] + 1, li[i * 2])
        if i * 3 <= n:
            li[i * 3] = min(li[i] + 1, li[i * 3])
    return li[n]
n = int(input())
print(bottomUp(n))
