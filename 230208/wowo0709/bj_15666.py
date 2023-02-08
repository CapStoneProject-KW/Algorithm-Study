from itertools import combinations_with_replacement as H

def solution(arr: list[int], m: int) -> list:
    sorted_arr = sorted(arr)
    ret = {h: True for h in H(sorted_arr, m)} # dict: keeps the order
    return list(ret.keys())


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = solution(arr, M)
    for seq in ans:
        print(*seq)