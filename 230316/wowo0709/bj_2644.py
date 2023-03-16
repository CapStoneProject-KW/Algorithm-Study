from collections import deque

def solution(graph: dict, src: int, dst: int, n: int):
    visited = [False for _ in range(n+1)]
    q = deque([(src, 0)])
    visited[src] = True
    while q:
        cn, cd = q.popleft()
        if cn == dst:
            return cd
        for an in graph[cn]:
            if not visited[an]:
                q.append((an, cd+1))
                visited[an] = True
    return -1


if __name__ == '__main__':
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    graph = {i: set() for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    print(solution(graph, a, b, n))
