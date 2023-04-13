import sys
from heapq import heappop, heappush
import math
sys.stdin = open("bj_18352_in.txt", "r")
input = sys.stdin.readline

def solution():
    h = [(0, X)] # distance, source node
    visited = [0] * (N+1)
    count = 0
    distance = {}
    for node in graph.keys():
        distance[node] = math.inf
    distance[X] = 0

    while h:
        cur_dis, cur_node = heappop(h)
        visited[cur_node] = 1

        for i in graph[cur_node]:
            if not visited[i]:
                if distance[i] > distance[cur_node] + 1:
                    distance[i] = distance[cur_node] + 1
                    heappush(h, (distance[i], i))
    
    answer = []
    for k, v in distance.items():
        if v == K:
            answer.append(k)
    answer.sort()

    if len(answer) == 0:
        print(-1)
    else:
        print(*answer, sep='\n')



N, M, K, X = map(int, input().split())

graph = {e: [] for e in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

solution()