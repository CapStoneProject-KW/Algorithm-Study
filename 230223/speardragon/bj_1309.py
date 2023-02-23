import sys
sys.stdin = open("bj_1309_in.txt", "r")
input = sys.stdin.readline
'''
DP
memo[N] = 경우의수

  1 2 3  4  5
  3 7 17 41

N=3일 때
1. N=2에 사자가 없는 경우 = f(1) - base case
2. N=2에 사자가 왼쪽에 있는 경우 = f(2)
3. N=2에 사자가 오른쪽에 있는 경우 = f(2)


f(n) = (f(n-1) * 2) + f(n-2)
'''



def solution(memo):
    memo[0] = 1
    memo[1] = 3

    for i in range(2, N+1):
        memo[i] = (memo[i-1]*2 + memo[i-2]) % 9901
    
    print(memo)
    return memo[N]
        



N = int(input())
_memo = [0] * (N+1)

print(solution(_memo))

