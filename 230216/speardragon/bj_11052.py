import sys
sys.stdin = open("bj_11052_in.txt", "r")
input = sys.stdin.readline
import math
'''
카드 i개가 포함된 카드팩 가격 Pi

rot-cutting 유사
memo[N: 구매하려는 카드 개수] = 최대 금액 

N=4:
1 3
2 2
3 1

f(n) = max(pi + f(n-1), pn)
base case: 
'''

def solution(num):
    if num == 0:
        return 0
    
    if _memo[num] == 0:
        max_value = -math.inf
        for i in range(1, num+1):
            price = cards[i] + solution(num-i)
            max_value = max(price, max_value)
        _memo[num] = max_value
    
    print(_memo)
    return _memo[num]
    

def solution2(num):
    for i in range(1, num+1):
        max_value = -math.inf
        for j in range(1, i+1):
            price = cards[j] + _memo[i-j]
            max_value = max(price, max_value)
        _memo[i] = max_value

    return _memo[num]

    

N = int(input())

cards = [0]
cards.extend(list(map(int, input().split())))
# cards = list(map(int, input().split()))
_memo = [0] * (N+1)

print(solution(N))



'''
bu가 더 빠름

'''