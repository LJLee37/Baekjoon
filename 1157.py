st = input()
l = len(st)
count = [0 for i in range(26)]
for i in st:
    count[ord(i.upper()) - 0x41] += 1
mi = 0
isDuplicate = False
for i in range(1, 26):
    if count[i] > count[mi]:
        mi = i
        isDuplicate = False
    elif count[i] == count[mi]:
        isDuplicate = True
print('?' if isDuplicate else chr(mi + 65))
