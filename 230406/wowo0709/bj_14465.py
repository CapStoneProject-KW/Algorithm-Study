def solution(roads: list[int], n: int, k: int) -> int:
    for i in range(1, n):
        roads[i] += roads[i-1]
    _max = 0
    for i in range(k, n):
        _max = max(roads[i] - roads[i-k], _max)
    return k - _max


if __name__ == '__main__':
    N, K, B = map(int, input().split())
    roads = [1 for _ in range(N)]
    for _ in range(B):
        roads[int(input())-1] = 0
    print(solution(roads, N, K))