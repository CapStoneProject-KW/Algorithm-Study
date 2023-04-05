import sys
sys.stdin = open("bj_17829_in.txt", "r")
input = sys.stdin.readline

def solution(matrix):
    if len(matrix) == 2:
        tmp = matrix[0] + matrix[1]
        return sorted(tmp, reverse=True)[1]
    
    else:
        while len(matrix) != 2:
            m = len(matrix)
            idx, jdx = 0, 0
            slice = [[0]*(m//2) for _ in range(m//2)]

            for i in range(0, m, 2):
                jdx = 0
                for j in range(0, m, 2):
                    slice[idx][jdx] = solution([row[j:j+2] for row in matrix[i:i+2]])
                    jdx+=1
                idx+=1
            matrix = slice[:]
    
    return solution(matrix)

def solution2(n, row, col):
    if n == 2:
        return sorted([_matrix[row][col], _matrix[row+1][col],\
                        _matrix[row][col+1], _matrix[row+1][col+1]], reverse=True)[1]
    else:
        mid = n // 2
        lt = solution2(mid, row, col)
        rt = solution2(mid, row, col+mid)
        lb = solution2(mid, row+mid, col)
        rb = solution2(mid, row+mid, col+mid)

    return sorted([lt, rt, lb, rb], reverse=True)[1]

N = int(input())

_matrix = [list(map(int, input().split())) for _ in range(N)]

print(solution2(N, 0, 0))