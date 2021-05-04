#constructer n < d(n)
nonSelfNum = [] # 셀프넘버가 아닌 수를 저장할 리스트.
i = 1 #91이 빌드하는 수는 101이므로 91부터 시작.
while i <= 10000: # 10000 이하의 수에 대해서
    newnum = i + sum(map(int,list(str(i)))) #새 수를 빌드.
    #print(f'newnum : {newnum}') #디버그용
    #input()
    if newnum not in nonSelfNum:
        nonSelfNum.append(newnum) #없으면 추가.
    nonSelfNum.sort() #수의 서순을 맞추기 위해 정렬.
    if len(nonSelfNum) <= 0 or i != nonSelfNum[0]: #i는 nonSelfNum[0]보다 반드시 작거나 같으므로
        print(i) #i가 nonSelfNum[0]가 아니거나 nonSelfNum에 수가 없다면 출력.
    else:
        nonSelfNum.pop(0) #i가 nonSelfNum[0]라면 출력을 건너뛰고 0삭제.
    i += 1
