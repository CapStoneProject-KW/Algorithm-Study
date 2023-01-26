from collections import deque

def solution(src: int, dst: int) -> int:
    # times = [None for _ in range(dst+1)] # OOM
    # times[src] = 1
    times = {src: 1}
    q = deque([(src, 1)])
    while q:
        cur_n, t = q.popleft()
        for next_n in [cur_n * 2, int(str(cur_n) + '1')]:
            if 0 <= next_n <= dst and not next_n in times:
                times[next_n] = t+1
                q.append((next_n, t+1))
        if dst in times:
            break
    return times[dst] if dst in times else -1


if __name__ == '__main__':
    A, B = map(int, input().split())
    print(solution(A, B))