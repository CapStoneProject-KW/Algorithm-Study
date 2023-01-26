from heapq import heappush, heappop

def solution(graph: list, items: list, start: int, d_limit: int) -> int:
    visited = [False for _ in range(len(graph))]
    # dists = [-1 for _ in range(len(graph))]
    heap = [(0, start)]
    while heap:
        d_total, cur_node = heappop(heap)
        visited[cur_node] = True
        # dists[cur_node] = d_total
        for d, adj_node in graph[cur_node]:
            if d_total + d <= d_limit and not visited[adj_node]:
                heappush(heap, (d_total + d, adj_node))
    return sum([items[i] for i in range(len(visited)) if visited[i]])
    # return sum([items[i] for i in range(len(dists)) if dists[i] > -1])


if __name__ == '__main__':
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    items = [0] + list(map(int, input().split()))
    for _ in range(R):
        a, b, l = map(int, input().split())
        graph[a].append((l, b))
        graph[b].append((l, a))
    ans = -1
    for start in range(1, N+1):
        ans = max(ans, solution(graph, items, start, M))
    print(ans)