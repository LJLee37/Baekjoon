N = int(input())
level = 1
currentLevelCounter = 2
COMMON_RATIO = 6
while N >= currentLevelCounter:
    currentLevelCounter += level * COMMON_RATIO
    level += 1
print(level)

"""
0, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, ...
2의 오른쪽 아래로 가면 레벨이 1 증가.
2의 오른쪽 아래로 가는 조건?
2, 8, 20, 38, 62, ...
2, 2+6, 2+6+12, 2+6+12+18, 2+6+12+18+24, ...
2, 2+6*1, 2+6*1+6*2, 2+6*1+6*2+6*3, 2+6*1+6*2+6*3+6*4, ...
현재 레벨을 저장하고 레벨 카운터를 만들어서 레벨 카운터 값을 N 이상까지 증가하면 레벨이 나온다.
해결!
"""
