import sys
sys.stdin = open("input_txt/bj_1904_in.txt", "r")
input = sys.stdin.readline
'''
f(1) = 1
1

f(2) = 2
00, 11

f(3) = 3
001, 100, 111

f(4) = 5
0011, 0000, 1001, 1100, 1111

일반적인 dp -> 메모리초과 -> 어떻게 해결?
'''


def solution():
    memo[1] = 1
    memo[2] = 2

    for i in range(3, N+1):
        memo[i] = (memo[i-1] + memo[i-2]) % 15746

    return memo[N] 


N = int(input())
memo = [0 for _ in range(1000001)] # N+1로 하면 indexerror 
print(solution())



# def solution2(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
    
#     if memo[n] == 0:
#         memo[n] = solution2(n-1) + solution2(n-2)

#     return memo[n]

# def solution():
#     memo[1] = 1
#     memo[2] = 2

#     for i in range(3, N+1):
#         memo[i] = memo[i-1] + memo[i-2]

#     return memo[N] % 15746
