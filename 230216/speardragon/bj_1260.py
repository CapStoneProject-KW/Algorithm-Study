import sys
from collections import deque
sys.stdin = open("bj_1260_in.txt", "r")
input = sys.stdin.readline
'''
재귀: 만나자마자
stack-while: 현재 인접한 거 다 넣어놓고 맨 처음부터

문제: 방문순서

f

'''

def dfs(idx):
    visited1[idx] = 1

    print(idx, end=' ')

    for i in range(1, N+1):
        if visited1[i] == 0 and graph[idx][i] == 1:
            dfs(i)

def dfs2(idx):
    s = []
    s.append(idx)
    visited1[idx] = 1

    while s:
        node = s.pop()
        print(node, end=' ')
        tmp = []
        for i in range(1, N+1):
            if visited1[i] == 0 and graph[node][i] == 1:
                # tmp.append(i)
                s.append(i)
                visited1[i] = 1
        # s += reversed(tmp)
        print(s)
    
def bfs(idx):
    q = deque()
    q.append(idx)
    visited2[idx] = 1

    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[node][i] == 1:
                q.append(i)
                visited2[i] = 1




N, M, V = map(int, input().rstrip().split())

graph = [[0] * (N+1) for _ in range(N+1)]

visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)

for i in range(M):
    fr, to = map(int, input().split())
    graph[fr][to] = 1
    graph[to][fr] = 1

dfs2(V)
print()
bfs(V)


'''
N=1000이면 1000개의 리스트가 만들어지는데 쓰이지도 않음 -> 딕셔너리로 어떻게?
'''