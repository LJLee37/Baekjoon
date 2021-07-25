# Ani ige moya.
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    #adjacentList = []
    '''
    for i in range(N):
        temp = [0 for j in range(N)]
        adjacentList.append(temp)
        '''
    for i in range(M):
        temp1, temp2 = map(int, input().split())
        #adjacentList[temp1 - 1][temp2 - 1] = 1
        #adjacentList[temp2 - 1][temp1 - 1] = 1
    #adjacentCount = [adjacentList[x].count(1) for x in range(N)]
    #least = 0
    '''
    for i in range(1, N):
        if adjacentCount[least] > adjacentCount[i]:
            least = i
'''
    print(N - 1)
