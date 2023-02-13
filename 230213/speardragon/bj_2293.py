import sys
sys.stdin = open("bj_2293_in.txt", "r")
input = sys.stdin.readline
'''
3, 5
1
2
5

1+1+1+1+1
1+1+1+2
1+2+2
5

1. 백트래킹

2. DP
f(1)=1
1

f(2)=1
1+1
2

f(3)=2
1+1+1
1+2

f(4)=3
1+1+1+1
1+1+2
2+2

f(5)=4
1+1+1+1+1
1+1+1+2
1+2+2
5

f(6)=4
111111
11112
122
15



'''
# result = []

# def solution(ans):
#     # print(ans)
#     if sum(ans) == k:
#         print(ans)
#         result.append(ans)
#         solution.count += 1
    
#     else:
#         for coin in coins:
#             if sum(ans) > 10: continue
#             # print(ans)
#             ans.append(coin)
#             solution(ans)
#             ans.pop()




# n, k = map(int, input().split())

# coins = [int(input()) for _ in range(n)]

# solution.count = 0
# solution([])
# print(solution.count)

def solution():
    memo[0] = 1
    for coin in coins:
        for i in range(coin, k+1):
            memo[i] += memo[i-coin]
    return memo[k]


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
memo = [0] * (k+1)

print(solution())