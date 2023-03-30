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

def solution(l, x):
    if l == 0:
        return 1
    
    


N, X = map(int, input().split())
hamburger = []

dp = [None]*51

answer = list(solution(N, X))
answer = sum(map(lambda x: x=="P", answer[len(answer)-X:]))
print(answer)