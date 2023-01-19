def solution(nums: list[int]) -> int:
    '''
    Description:
        Compute the max length of increasing sequence in the list
    Args:
        nums: list consisted of integers
    Ret:
        Max length of increasing sequence in the list
    '''
    lis = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
    return max(lis)


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(solution(nums))