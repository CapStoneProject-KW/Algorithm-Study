import sys
from collections import deque
sys.stdin = open("bj_2667_in.txt", "r")
input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j):
  count = 1
  q = deque([(i, j)])
  
  visited[i][j] = True

  while q:
    cur_i, cur_j = q.popleft()
    for di, dj in move:
      new_i, new_j = cur_i+di, cur_j+dj
      if (not (0 <= new_i < N)) or (not (0 <= new_j < N)): 
        continue
      if (visited[new_i][new_j] == True) or (graph[new_i][new_j] != 1):
        continue
      # print("new", new_i, new_j)
      q.append((new_i, new_j))
      visited[new_i][new_j] = True
      count += 1
  # print(count)
  result.append(count)


    
N = int(input())

graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

num = 0
result = []
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1 and visited[i][j] == False:
      bfs(i, j)
      num += 1

print(num)
result.sort()
print(*result, sep="\n")
        