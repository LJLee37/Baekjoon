L = int(input())
s = input()
retval = 0
for i in range(L):
    retval += (ord(s[i]) - 0x60) * (31 ** i)
    retval %= 1234567891
print(retval)
