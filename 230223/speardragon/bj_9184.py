import sys
sys.stdin = open("bj_9184_in.txt", "r")
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        if a == b == c == -1:
            return -1
        answer = 1
        return answer
    
    elif a > 20 or b > 20 or c > 20:
        answer = w(20, 20, 20)
        return answer
    
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


answer = 0
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while answer != -1:
    a, b, c = map(int, input().split())

    answer = w(a, b, c)

    if answer == -1:
        break
    print(f"w({a}, {b}, {c}) = {answer}")



    
