import sys
from itertools import combinations_with_replacement as H
sys.stdin = open("bj_15652_in.txt", "r")
input = sys.stdin.readline
'''
어디서 많이 본 문제...?

'''

def solution():
    ans = [i for i in range(1, N+1)]

    for h in H(ans, M):
        print(*h)



N, M = map(int, input().split())

solution()