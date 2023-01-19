'''
예상 알고리즘 분류: 브루트 포스(완전 탐색)

1. M x N 크기 보드
  ㄴ 잘라서 8x8 체스판으로 사용
  ㄴ 체스판은 검, 흰 번갈아 있어야 함.
  ㄴ 두 가지 경우
    ㄴ맨 첫 칸이 흰 or 검

2. 잘라진 여러 개의 8x8 미완성 체스판이 나올텐데
   그 중에서 가장 조금만 수정하면 되는 체스판의 수정 횟수

3. for문을 돌면서 왼쪽 위 모서리가 지정되면 체스판 하나가 만들어짐.
  ㄴ 근데 길이가 8이 안되는 애들은 거름
  ㄴ 가로: board[1][i], 세로: board[i][0]

4. 잘라진 보드판에서도 두 가지 경우 존재
  ㄴ 왼쪽 위 모서리가 B or W
  ㄴ 둘 다 판단해 봐서 더 적은 애 리턴

5. B이면 짝수 col B, 짝수 row B

6. 행이 현재 짝수(0,2,...)이고 열이 짝수인곳에 B
   행이 현재 홀수이고 열이 홀수인곳에 B
'''
import sys
global board
global N, M


def sol(row: int, col: int):
  chess_board = [result_board[col:col+8] for result_board in board[row:row+8]]

  first_black_count = 0
  first_white_count = 0

  for i in range(8):
    for j in range(8):
      black_check_1 = i % 2 == 0 and ((j % 2 == 0 and chess_board[i][j] != 'B') or (j % 2 != 0 and chess_board[i][j] != 'W'))
      black_check_2 = i % 2 != 0 and ((j % 2 == 0 and chess_board[i][j] != 'W') or (j % 2 != 0 and chess_board[i][j] != 'B'))
      white_check_1 = i % 2 == 0 and ((j % 2 == 0 and chess_board[i][j] != 'W') or (j % 2 != 0 and chess_board[i][j] != 'B'))
      white_check_2 = i % 2 != 0 and ((j % 2 == 0 and chess_board[i][j] != 'B') or (j % 2 != 0 and chess_board[i][j] != 'W'))
      
      if black_check_1 or black_check_2:
        first_black_count += 1
      if white_check_1 or white_check_2:
        first_white_count += 1

  return min(first_black_count, first_white_count)


sys.stdin = open('bj_1018_in.txt', 'r')

N, M = map(int, input().split())

board = []
for i in range(N):
  board.append(list(input()))

minimum_value = 3000

# 체스판 자르기
for i in range(N):
  for j in range(M):
    if j <= (M - 8) and i <= (N - 8): # 가로, 세로 범위 만족
      minimum_value = min(minimum_value, sol(i, j))

print(minimum_value)

'''
2차원 리스트 슬라이싱

'''