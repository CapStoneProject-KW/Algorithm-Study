'''
현재까지의 최댓값 = 
현재를 택했을 때 다음으로 가능한 시간까지의 최댓값 or
현재를 택하지 않았을 때 다음 시간의 최댓값
0 1  2  3  4  5  6  7 8
X 45 45 45 35 15 0  0 X
=> 거꾸로 계산!
'''

def solution(n: int, times: int, prices: int) -> int:
    times = [0] + times + [0] # dummy
    prices = [0] + prices + [0] # dummy
    dp = [0 for _ in range(n+2)]
    for t in range(n, 0, -1):
        nt = t + times[t] 
        if nt > n+1:
            dp[t] = dp[t+1]
        else:
            dp[t] = max(prices[t]+dp[nt], dp[t+1])
    return dp[1]


if __name__ == '__main__':
    N = int(input())
    times, prices = [], []
    for i in range(N):
        t, p = map(int, input().split())
        times.append(t)
        prices.append(p)
    print(solution(N, times, prices))