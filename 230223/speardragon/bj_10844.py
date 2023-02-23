import sys
sys.stdin = open("bj_10844_in.txt")
input = sys.stdin.readline
'''
길이가 N인 계단수
0
10 12
21 23 
32 34 
43 45
54 56
65 67
76 78
87 89
98

101 121 123
210 212 232 234 
32 34 
43 45
54 56
65 67
76 78
87 89
98

28

f(1) = 9
f(2) = 17
f(3) = 

dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]
N번째 자리수의 K로 끝나는 계단 수의 갯수는
그 전단계(N-1)의 끝자리(N번째에서 보면 끝에서 두번째 숫자)가 K+1, K-1인 
경우의 합

예외) N=0, N=9 -> 각각 dp[n-1][1], dp[n-1][8]
'''
def solution(dp):
    for i in range(1, 10):
        dp[1][i] = 1


    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(dp)
      
    return sum(dp[N]) % 1000000000
        


N = int(input())

_dp = [[0]*10 for _ in range(N+1)]

print(solution(_dp))

