'''
1: 1
2: 10
3: 100, 101
4: 1010, 1000, 1001
5: 10100, 10000, 10010, 10101, 10001
...
=> 맨 뒤에 0은 다 붙일 수 있고, 0으로 끝나는 수는 1도 붙일 수 있다. 
=> 0을 다 붙이고 (dp[n-1]) + 1을 다 붙이고 (= 0으로 끝나는 수 = dp[n-2])
=> dp[n] = dp[n-1] + dp[n-2]
'''
def solution(n: int) -> int:
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == '__main__':
    N = int(input())
    print(solution(N))