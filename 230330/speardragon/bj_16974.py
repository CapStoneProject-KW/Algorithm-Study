import sys
sys.stdin = open("bj_16974_in.txt", "r")
input = sys.stdin.readline
'''
레벨L버거
    번 + L-1 + 패티 + L-1 + 번

    빵
    solution(L-1)
    패티
    solution(L-1)
    빵

시간초과 -> DP?
dp[N] = 'BPPB'

메모리초과? -> 레벨이 커질수록 리스트가 너무 길어짐
-> 반만 확인


'''


# def solution(L):
#     if L == 0:
#         return "P"
    
#     if dp[L] is None:
#         tmp = solution(L-1)
#         dp[L] = "B" + tmp + "P" + tmp + "B"
#     return dp[L]

def solution(level, x):
    l, p = hamburger[level]
    if x == 0:
        return 0
    if x == l:
        return p
    elif x >= l//2+1:
        return solution(level-1, x-(l//2+1)) + 1 + hamburger[level-1][1]
    elif x == l//2:
        return hamburger[level-1][1]
    else:
        return solution(level-1, x-1)


N, X = map(int, input().split())
hamburger = [[1, 1]] # 길이, 패티

for i in range(1, N+1):
    hamburger.append([3+hamburger[i-1][0]*2, 1+hamburger[i-1][1]*2])

print(solution(N, X))