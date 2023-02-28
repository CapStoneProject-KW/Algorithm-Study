import sys
from collections import deque
sys.stdin = open("bj_1012_in.txt")
input = sys.stdin.readline
'''
BFS-q
'''

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(cur):
    i, j = cur[0], cur[1]
    q = deque()
    q.append((i, j))

    if visited[i][j]:
        return

    visited[i][j] = True
    
    # graph[i][j] = 0

    while q:
        ci, cj = q.popleft()
        for di, dj in move:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and graph[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = True
                # print(visited)
                q.append((ni, nj))
        


T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    # print(graph)
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] or graph[i][j] == 0:
                continue
            bfs((i,j))
            # print(visited)
            count += 1
            
    
    print(count)
        
    