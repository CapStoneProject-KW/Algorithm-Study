import sys
from heapq import heappop, heappush, heapify
from math import ceil
sys.stdin = open("bj_1417_in.txt", "r")
input = sys.stdin.readline
'''
어떤 특정 사람보다 많아질 때까지 가져옴
나보다 크면 그 차이만큼 더한다.
5 10
8 7
6 10
8 8
'''
def solution(votes):
    dasom = votes[0]
    answer = 0
    while any(dasom <= votes[i] for i in range(1,N)):
        for i in range(1, N):
            if votes[i] > dasom:
                tmp = ceil((votes[i] + dasom) / 2) # objective
                votes[i] -= tmp - dasom
                answer += tmp - dasom
                dasom = votes[0] = tmp
            elif votes[i] == dasom:
                votes[0] = dasom = votes[i] + 1
                votes[i] = votes[i] - 1
                answer += 1
    return answer

def solution2(votes):
    answer = 0
    dasom = votes[0]
    h = []

    for i in votes[1:]:
        heappush(h, -i)

    print(h)

    while h:
        print(h, dasom)
        cur = -heappop(h)
        if dasom <= cur:
            dasom += 1
            answer += 1
            heappush(h, -(cur-1))

    return answer 


N = int(input())
votes = [int(input()) for _ in range(N)]

print(solution2(votes))


