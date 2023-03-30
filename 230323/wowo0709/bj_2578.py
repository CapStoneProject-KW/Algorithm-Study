def solution(board: list[int], nums: list[int]) -> int:
    # 0~4: rows, 5~9: cols, 10, 11: diags
    bingo = [0 for _ in range(12)]
    for t in range(len(nums)):
        idx = board.index(nums[t])
        i, j = idx // 5, idx % 5
        bingo[i] += 1
        bingo[5+j] += 1
        if i == j: bingo[10] += 1
        if i+j == 4: bingo[11] += 1
        if bingo.count(5) >= 3: break
    return t+1


if __name__ == '__main__':
    board = [] # 1-d list
    for _ in range(5):
        board += list(map(int, input().split()))
    nums = [] # 1-d list
    for _ in range(5):
        nums += list(map(int, input().split()))
    print(solution(board, nums))
