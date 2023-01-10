from heapq import heappush, heappop

def solution(start: int, end: int) -> int:
    '''
    Description:
        Compute how much time is needed to go from start to end
    Args:
        start: start point
        end: end point
    Ret:
        Minimum time to reach the endpoint
    '''
    points = [-1 for _ in range(100001)]
    points[start] = 0
    # dijkstra: Have to search the points which need lower time(cost) to reach first
    # We use dijkstra algorithm when different time/cost is assigned to each
    h = []
    heappush(h, (0, start))
    while h:
        time, cur = heappop(h)
        nexts = [(cur*2, points[cur]), (cur+1, points[cur]+1), (cur-1, points[cur]+1)]
        for next, time in nexts:
            if 0 <= next <= 100000 and points[next] == -1:
                points[next] = time
                heappush(h, (time, next))
        if points[end] > -1:
            break
    return points[end]


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solution(N, K))