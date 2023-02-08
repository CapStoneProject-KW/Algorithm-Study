'''
물이 새는 곳의 위치를 오름차순 정렬하고, 
작은데부터 탐색하면서
물이 새는 곳에 테이프를 붙이고 다음 위치로 이동
끝까지 이동하면 끝
'''
def solution(tape_len: int, locs: list[int]) -> int:
    sorted_locs = sorted(locs)
    cur, next_idx, cnt = 1, 0, 0
    while next_idx < len(locs):
        if sorted_locs[next_idx] == cur:
            cur += tape_len
            cnt += 1
            while next_idx < len(locs) and sorted_locs[next_idx] < cur:
                next_idx += 1
        else:
            cur += 1
    return cnt


if __name__ == '__main__':
    N, L = map(int, input().split())
    locs = list(map(int, input().split()))
    print(solution(L, locs))