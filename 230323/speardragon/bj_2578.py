import sys
sys.stdin = open("bj_2578_in.txt", "r")
input = sys.stdin.readline
import pprint

def find(x): # 선형탐색
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == x:
                return i, j

def is_bingo(check):
    is_three = 0

    for i in check:
        if all(i): is_three += 1
        
    for i in zip(*check):
        if all(i): is_three += 1

    diag1 = [check[i][j] for j in range(5) for i in range(5) if i == j]
    diag2 = [check[i][j] for j in range(5) for i in range(5) if i+j==4]

    if all(diag1): is_three += 1
    if all(diag2): is_three += 1

    # print(is_three)

    return is_three >= 3 # 너였구나.....................

def solution():
    count = 0
    for i in range(5):
        for j in range(5):
            r, c = find(erase[i][j])
            check[r][c] = 1
            count += 1
            # print(r, c)
            # pprint.pprint(check)
            if is_bingo(check):
                # print('빙고!')
                return count


bingo = [list(map(int, input().split())) for _ in range(5)]
erase = [list(map(int, input().split())) for _ in range(5)]
check = [[0]*5 for _ in range(5)]

# print(help(all))

print(solution())