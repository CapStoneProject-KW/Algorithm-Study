import sys
sys.stdin = open("bj_2225_in.txt", "r")
input = sys.stdin.readline
'''
N=20
K=2

0~20까지의 정수 중 2개를 더해서 그 합이 20이 되는 경우의 수

0, 20
1, 19
...
9, 11
10, 10

0, 21
10, 11
11, 10

sol1) 재귀 -> 시간초과
sol2) DFS? -> X
sol3) 알고리즘 분류 확인 -> DP?!


N=3, K=2
3을 2개로 나눈다.
 - 03, 12, 21, 30
[0+(3을 1개로 나눈 것)] + [1+(2를 1개로 나눈 것)] + [2+(1을 1개로 나눈 것)] + [3+(0을 1개로 나눈 것)]

    0 1 2 3 4 5 
0 | 1
1 | 1 1 1 1 1 1
2 | 1 2 3 4 
3 | 1 3

dp[n][k] = dp[0][k-1] + dp[1][k-1] + ... dp[n][k-1]

dp[n][j] = dp[n-1][k] + dp[n][k-1]
dp[0][1] = dp[-1][1] + dp[0][0]

'''

# def solution(ans):
    
#     if len(ans) == K:
#         if sum(ans) == N:
#             # print(ans)
#             solution.count += 1
#         return 
    
#     for i in range(N+1):
#         ans.append(i)
#         solution(ans)
#         ans.pop()
    

def solution(memo):
    memo[0][0] = 1
    
    for i in range(0, N+1):
        for j in range(1, K+1):
            memo[i][j] = (memo[i-1][j] + memo[i][j-1]) % 1000000000
            # print(i, j, memo[i][j])
    
    return memo[N][K]




N, K = map(int, input().split())
# solution.count = 0

_memo = [[0]*(K+1) for _ in range(N+1)]
print(solution(_memo))

# print(solution.count % 1000000000)