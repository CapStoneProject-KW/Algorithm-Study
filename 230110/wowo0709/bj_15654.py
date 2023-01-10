from itertools import permutations as P

def solution(nums: list[int], k: int) -> None:
    '''
    Description:
        Print permutations of given integer list alphabetically
    Args:
        nums: integer list
        k: length of each permutation
    '''
    sorted_nums = sorted(nums)
    for p in P(sorted_nums, k):
        print(*p)


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    solution(nums, M)