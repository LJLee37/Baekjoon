N = int(input())
S, M, L, XL, XXL, XXXL = [int(x) for x in input().split()]
tshirts = [S, M, L, XL, XXL, XXXL]
T, P = [int(x) for x in input().split()]
import math

tshirtsOrders = 0
for tshirt in tshirts:
    tshirtsOrders += math.ceil(tshirt / T)
penOrders = N // P
penRemainders = N % P
print(tshirtsOrders)
print(penOrders, penRemainders)
