import sys
sys.stdin = open("bj_9663_in.txt", "r")
input = sys.stdin.readline
'''
백트래킹

column 별로 놓을 수 있는 공간 찾기
- 현재 위치에서 대각선에 있는 것은 X
- 같은 행 X

index: col
value: 그 열에서 몇 번째 행인지

ㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁ

'''

def solution(depth):
    if depth == N:
        solution.count += 1
        return

    for i in range(N):
        arr[depth] = i
        if move_check(depth):
            solution(depth+1)

def move_check(col):
    for i in range(col):
        if arr[col] == arr[i]:
            return False
        elif abs(col-i) == abs(arr[col]-arr[i]):
            return False
    
    return True


N = int(input())

arr = [0] * N

solution.count = 0

solution(0)
print(solution.count)
