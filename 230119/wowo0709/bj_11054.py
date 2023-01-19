def solution(nums: list[int]) -> int:
    '''
    Description:
        Compute the max length of bitonic sequence in the list
    Args:
        nums: list consisted of integers
    Ret:
        Max length of bitonic sequence in the list
    '''
    N = len(nums)
    f_lis = [1 for _ in range(len(nums))] # forward
    b_lis = [1 for _ in range(len(nums))] # backward
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and f_lis[j] + 1 > f_lis[i]:
                f_lis[i] = f_lis[j] + 1
            if nums[N - (i+1)] > nums[N - (j+1)] and b_lis[N - (i+1)] < b_lis[N - (j+1)] + 1:
                b_lis[N - (i+1)] = b_lis[N - (j+1)] + 1
    lbs =  [x+y-1 for x, y in zip(f_lis, b_lis)]
    return max(lbs)


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(solution(nums))