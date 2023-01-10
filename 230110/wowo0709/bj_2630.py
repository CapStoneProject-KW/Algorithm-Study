import sys
input = sys.stdin.readline
global papers

def solution(size: int, row: int, col: int, ans: list[int]) -> list[int]:
    '''
    Description:
        Count white and blue papers in (size x size) shaped square
    Args:
        size: length of a side of the square
        row: start index of row
        col: start index of column
        ans: [white, blue]
    Return:
        Total # of white and blue papers [white, blue]
    '''
    paper = papers[row][col]
    # Base case
    if size == 1:
        return [ans[0]+1, ans[1]] if paper == 0 else [ans[0], ans[1]+1]
    # General case
    all_same = True
    for i in range(row, row + size):
        for j in range(col, col + size):
            if papers[i][j] != paper:
                all_same = False
                break
        if not all_same: 
            break
    if all_same:
        return [ans[0]+1, ans[1]] if paper == 0 else [ans[0], ans[1]+1]
    else:
        return list(sum(cnts) for cnts in zip(solution(size // 2, row, col, ans),
                                    solution(size // 2, row, col + (size // 2), ans), 
                                    solution(size // 2, row + (size // 2), col, ans), 
                                    solution(size // 2, row + (size // 2), col + (size // 2), ans)))


if __name__ == '__main__':
    N = int(input())
    papers = []
    for _ in range(N):
        papers.append(list(map(int, input().rstrip().split())))
    print(papers)
    print(*solution(N, 0, 0, [0, 0]), sep='\n')