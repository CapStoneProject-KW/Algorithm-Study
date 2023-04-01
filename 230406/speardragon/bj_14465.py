import sys
sys.stdin = open("bj_14465_in.txt", "r")
input = sys.stdin.readline
'''
1 2 3 4 5 6 7 8 9 10
x x 3 4 x 6 7 8 x x

예외:
x x 3 4 5 x 7 8 x x

K개의 구간 확인
l[6] - 0
l[6] - l[1]

'''

'''시간초과'''
def solution():
    l = [0] + [0 if i in broken else 1 for i in range(1, N+1)]
    
    part_sum, answer = 0, 0

    part_sum = sum(l[:K])
    answer = K - part_sum

    for i in range(K, N): # 6 ~ 9
        # part_sum = l[i-K+1] - l[i]
        part_sum = sum(l[i-K+1:i+1])
        # print(part_sum)
        answer = min(answer, K - part_sum)
    
    return answer

def solution2():
    l = [0] + [0 if i in broken else 1 for i in range(1, N+1)]

    for i in range(1, N+1): # 누적합
        l[i] = l[i-1] + l[i]

    answer = 0
    for i in range(K, N+1): # 부분합, 6~10
        answer = max(l[i] - l[i-K], answer)

    return K - answer



N, K, B = map(int, input().split())

broken = [int(input()) for _ in range(B)]

print(solution2())