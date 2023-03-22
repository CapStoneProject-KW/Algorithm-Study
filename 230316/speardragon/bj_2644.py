import sys
from collections import deque
sys.stdin = open("bj_2644_in.txt")
input = sys.stdin.readline
'''
촌수 계산
1. 부모-자식: 1촌
2. 할아버지-아버지-나: 2촌
3. 아버지 형제-할아버지: 1촌
4. 나-아버지 형제: 3촌

친척 관계가 없으면 -1

사이클이 발생하지 않기 때문에 트리 구조라서 dfs 시 visited를 다시 돌려놓는 과정이 없어도 됨
'''
def solution(people, A, B, m, relation):
    start, dest = min(A, B), max(A, B)
    # start, dest = 1, 3 # 부모-자식
    visited = {e: 0 for e in range(people+1)}
    q = deque([start])

    while q:
        cur = q.popleft()
        for child in relation[cur]:
            if child == dest:
                return visited[cur] + 1
            if not visited[child]:
                visited[child] = visited[cur] + 1
                print(visited)
                q.append(child)

    return -1 #if visited[dest] == 0 else visited[dest]


n = int(input())
A, B = map(int, input().split())
m = int(input())
# relation = [list(map(int, input().split())) for _ in range(m)]

relation = {e: [] for e in range(1, n+1)}

for i in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
    
    
print(A, B)
print(relation) #{1: [2, 3], 2: [7, 8, 9], 3: [], 4: [5, 6], 5: [], 6: [], 7: [], 8: [], 9: []}
print(solution(n, A, B, m, relation))

