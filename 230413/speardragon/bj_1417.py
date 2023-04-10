import sys
from heapq import heappop, heappush, heapify
sys.stdin = open("bj_1417_in.txt", "r")
input = sys.stdin.readline
'''
어떤 특정 사람보다 많아질 때까지 가져옴
'''


N = int(input())
votes = [int(input()) for _ in range(N)]

dason = votes[0]




