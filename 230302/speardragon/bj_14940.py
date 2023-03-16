import sys
from collections import deque
sys.stdin = open("bj_14940_in.txt", "r")
input = sys.stdin.readline

move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def solution(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0

    while q:
        ci, cj = q.popleft()
        for di, dj in move:
            ni, nj = ci+di, cj+dj
            if (0 <= ni < n) and (0 <= nj < m) and visited[ni][nj] == -1: 
                if graph[ni][nj] == 1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))
                elif graph[ni][nj] == 0:
                    visited[ni][nj] = 0
    
    

n, m = map(int, input().split())

graph = []
visited = [[-1 for _ in range(m)] for _ in range(n)]
# print(graph)

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_i, start_j = i, j

solution(start_i, start_j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
        