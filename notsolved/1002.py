def change2circles2singleVarEquation(x1, y1, r1, x2, y2, r2):
    alpha = x2 - x1
    beta = y2 - y1
    gamma = (r1 + r2) * (r1 - r2) / 2
    if beta != 0:
        return (1 + alpha**2/beta**2, 2*(alpha*gamma/beta**2 - x1 - y1*alpha / beta), x1 ** 2 + y1 ** 2 - r1 ** 2 - 2*y1*gamma / beta + gamma ** 2 / beta ** 2, 1 + alpha**2/beta**2, 2*(alpha*gamma/beta**2 - x1 - y2*alpha / beta), x2 ** 2 + y2 ** 2 - r2 ** 2 - 2*y2*gamma / beta + gamma ** 2 / beta ** 2)
    return -gamma / alpha


def solve2DEquation(a, b, c):
    if b ** 2 - 4*a*c > 0:
        return 2
    elif b ** 2 - 4 * a * c == 0:
        return 1
    else:
        return 0


T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = 0
    if y1 == y2:
        if x1 == x2:
            if r1 == r2:
                print(-1)
            else:
                print(0)
            continue
        else:
            distance = abs(x1 - x2)
    elif x1 == x2:
        distance = abs(y1 - y2)
    else:
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance == r1 + r2:
        print(1)
    elif distance > r1 + r2:
        print(0)
    else:
        print(2)
