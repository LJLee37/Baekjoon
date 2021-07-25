S = input()
alphabetIndexes = [-1] * 26
for i in range(len(S)):
    if S[i] != ' ':
        if alphabetIndexes[ord(S[i]) - ord('a')] == -1:
            alphabetIndexes[ord(S[i]) - ord('a')] = i
for i in alphabetIndexes:
    print(i, end=' ')
