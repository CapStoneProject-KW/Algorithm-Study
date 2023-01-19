# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
tray = [[0] * M for _ in range(N)]

# 그래프를 저장하기 위한 2차원 배열
count = [[]]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(graph,x,v,visited) :
    visited[v] = True
    global count
    count[x].append(v)
    for k in graph[v]:
        if not visited[k]:
            DFS(graph, x, k, visited)

def check(x,y):
    global count
    for h in range(4):
        nx = x + dx[h]
        ny = y + dy[h]
        if tray[nx,ny] == 0 and count


# 전체 노드 탐색
for i in range(N):
    for j in range(M):


