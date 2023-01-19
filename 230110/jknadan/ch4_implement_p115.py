C, R = input().split()

rowList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

case1 = 0
case2 = 0
result = 0

for j in range(2):

    if j == 0:
        i = rowList.index(C) + 1  # a~h 열 인덱스
        k = int(R)
        print(i, k)
        if 2 < i < 7:
            case1 = 2
        if k > 1:
            case2 = 2
        if i <= 2 or i > 7:
            case1 = 1
        if k == 1:
            case2 = 1
        result += case1 * case2
        print(result)
    elif j == 1:
        k = rowList.index(C) + 1
        i = int(R)
        print(i, k)
        if 2 < i < 7:
            case1 = 2
        if k > 1:
            case2 = 2
        if i <= 2 or i > 7:
            case1 = 1
        if k == 1:
            case2 = 1
        result += case1 * case2
        print(result)

print(result)
