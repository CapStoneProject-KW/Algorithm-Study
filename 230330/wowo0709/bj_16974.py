def solution(level: int, x: int) -> int:
    l, p = burgers[level]
    '''Sol 1'''
    if x <= 0:
        return 0
    if x >= l:
        return p
    return solution(level-1, x - (l//2 + 1)) + (x > l//2) + solution(level-1, x - 1)
    '''Sol 2'''
    # # x: 0 ~ l
    # if x == 0:
    #     return 0
    # if x == l:
    #     return p
    # elif x >= l//2 + 1:
    #     return solution(level-1, x - (l//2 + 1)) + 1 + burgers[level-1][1]
    # elif x == l//2:
    #     return burgers[level-1][1]
    # else:
    #     return solution(level-1, x - 1)


if __name__ == '__main__':
    global burgers
    N, X = map(int, input().split())
    burgers = [[1, 1]] # 버거의 길이, 패티의 개수
    for i in range(1, N+1):
        burgers.append([3+2*burgers[i-1][0], 1+2*burgers[i-1][1]])
    print(solution(N, X))