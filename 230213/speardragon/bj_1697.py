import sys
from heapq import heappush, heappop
from collections import deque
sys.stdin = open("input_txt/bj_1697_in.txt", "r")
input = sys.stdin.readline

'''
1, 2, 3, 4, 5, 6

'''


def bfs(start, end):
  q = deque([start])
  points = [-1 for _ in range(100001)]

  points[start] = 0

  while q:
    cur = q.popleft()
    if cur == end:
       return points[cur]
    for dn in [cur+1, cur-1, cur*2]:
       if 0 <= dn <= 100000 and points[dn] == -1:
          points[dn] = points[cur] + 1
          q.append(dn)
          

def solution(start, end):
    points = [-1 for _ in range(100001)]
    points[start] = 0

    h = []
    heappush(h, (0, start))

    while h:
        time, cur = heappop(h)
        nexts = [(cur*2, points[cur]+1), (cur+1, points[cur]+1), (cur-1, points[cur]+1)]
        for next, time in nexts:
            if 0 <= next <= 100000 and points[next] == -1:
                points[next] = time
                heappush(h, (time, next))
        if points[end] > -1:
            break
    
    return points[end]
                


N, K = map(int, input().split())

# print(solution(N, K))
print(bfs(N, K))