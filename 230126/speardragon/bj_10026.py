import sys
import copy
from collections import deque
sys.stdin = open("bj_10026_in.txt", "r")
input = sys.stdin.readline


def BFS(graph: list[list[str]], i: int, j: int):
  move = [(0, -1), (-1, 0), (0, 1), (1, 0)]
  color = graph[i][j] # 현재 내 컬러 기록
  graph[i][j] = 'X'

  q = deque()
  q.append((i, j))

  while q:
    cur_i, cur_j = q.popleft()
    for di, dj in move:
      next_i = cur_i + di
      next_j = cur_j + dj
      
      if not check_move(graph, next_i, next_j, color): # can move
        continue

      # print(next_i, next_j)
      graph[next_i][next_j] = 'X'
      q.append((next_i, next_j))
    # print(q)


def check_move(graph, i, j, color):
  if i < 0 or i >= N:
    return False
  if j < 0 or j >= N:
    return False
  if graph[i][j] != color:
    return False
  if graph[i][j] == 'X':
    return False

  return True



N = int(input())

_graph = [list(input().strip()) for _ in range(N)]

blind_graph = copy.deepcopy(_graph)
non_blind_graph = copy.deepcopy(_graph)


# 적록색맹 전처리
for i in range(N):
  for j in range(N):
    if blind_graph[i][j] == 'R': # Red를 Green으로
      blind_graph[i][j] = 'G'

# 적록 색맹 BFS
blind_cnt = 0
for i in range(N):
  for j in range(N):
    if not blind_graph[i][j] == 'X':
      BFS(blind_graph, i, j)
      blind_cnt += 1

# 정상인 BFS
non_blind_cnt = 0
for i in range(N):
  for j in range(N):
    if non_blind_graph[i][j] != 'X':
      BFS(non_blind_graph, i, j)
      non_blind_cnt += 1

print(non_blind_cnt, blind_cnt)

