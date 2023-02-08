from itertools import permutations as P

def solution(arr: list[int], m: int) -> list:
    sorted_arr = sorted(arr)
    ret = {p: True for p in P(sorted_arr, m)} # dict: keeps the order
    return list(ret.keys())


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = solution(arr, M)
    for seq in ans:
        print(*seq)