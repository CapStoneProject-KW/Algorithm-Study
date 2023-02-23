import sys
from itertools import permutations as P
sys.stdin = open("bj_2217_in.txt")
input = sys.stdin.readline
'''
로프의 갯수 k개로 들어올릴 수 있는 물체의 최대 중량
- 중량: w/k

10, 15
10만큼을 들어올릴 수 있는 로프 + 15만큼을 들어올릴 수 있는 로프

위 경우 최대 10의 하중을 견디도록 설계 -> 20kg를 2개로

greedy approach: 현재 물체의 무게를 어떤 방법으로든 견디지 못할 때까지 최신화
- case: 2개로 하는 경우 | 1개를 선택하여 하는 경우

10, 20, 30
-> 20,30 -> 40
10, 20, 30, 40, 50
-> 30-40-50 -> 90

for문 돌면서 본인 포함하여 뒤에 몇 개가 있는지 X 본인

'''
# def solution(min_lope, max_lope):
#     result = 0
    
#     for i in range(1, N+1):
#         result = max(min_lope * i, max_lope)
    
#     print(result)

# def solution2():
    
#     for i in range(1, N+1):
#         for p in P(lopes, i):
#             p = list(p)
#             print(p)


def solution3(lopes):
    max_weight = -1

    for i in range(N):
        max_weight = max((N-i) * lopes[i], max_weight)
    
    print(max_weight)

N = int(input())

lopes = [int(input().rstrip()) for _ in range(N)]
lopes.sort()

# min_lope = min(lopes)
# max_lope = max(lopes)

# solution(min_lope, max_lope)
solution3(lopes)

    
    

